import os
from fnmatch import fnmatch
from os import listdir
from os.path import join, isfile
from PyQt5 import QtGui
import config
import cpu_computing, gpu_computing
from utils import pixmap_to_image_with_format, matrix_to_pixmap
from threading import Thread, Condition
from queue import Queue


def read(path, files_to_treatment, treatment_condition):
    for f in listdir(path):
        cur_path = join(path, f)
        if isfile(cur_path) and (fnmatch(f, "*.png") or fnmatch(f, "*.jpg") or fnmatch(f, "*.jpeg")):
            files_to_treatment.put(pixmap_to_image_with_format(QtGui.QPixmap(cur_path)))
            treatment_condition.acquire()
            treatment_condition.notify()
            treatment_condition.release()

    files_to_treatment.put(0)
    treatment_condition.acquire()
    treatment_condition.notify()
    treatment_condition.release()


def treatment(filters_matrices, on_cpu, files_to_treatment, files_to_save, treatment_condition, save_condition):
    while True:
        if not files_to_treatment.empty():
            cur = files_to_treatment.get()

            if cur == 0:
                files_to_save.put(0)
                save_condition.acquire()
                save_condition.notify()
                save_condition.release()
                break

            if on_cpu:
                result = cpu_computing.apply_filters_to_matrix(cur[0], filters_matrices)
            else:
                result = gpu_computing.apply_filters_to_matrix(cur[0], filters_matrices)

            files_to_save.put(matrix_to_pixmap(result, cur[1]))
            save_condition.acquire()
            save_condition.notify()
            save_condition.release()
        else:
            treatment_condition.acquire()
            treatment_condition.wait(1000)
            treatment_condition.release()


def save(path, files_to_save, save_condition):
    number = len(listdir(path))
    while True:
        if not files_to_save.empty():
            cur = files_to_save.get()

            if cur == 0:
                break

            cur.save(f"{path}/file{number + 1}.png")
            number += 1
        else:
            save_condition.acquire()
            save_condition.wait(1000)
            save_condition.release()


def compute(path, filters_matrices_list, on_cpu):
    directory_to_save = config.directory_to_save
    if not os.path.exists(directory_to_save):
        os.mkdir(directory_to_save)

    files_to_treatment = Queue()
    files_to_save = Queue()
    treatment_condition = Condition()
    save_condition = Condition()

    r = Thread(target=read, args=(path, files_to_treatment, treatment_condition,))
    t = Thread(target=treatment,
               args=(filters_matrices_list, on_cpu, files_to_treatment, files_to_save,
                     treatment_condition, save_condition,))
    s = Thread(target=save, args=(directory_to_save, files_to_save, save_condition,))

    r.start()
    t.start()
    s.start()

    r.join()
    t.join()
    s.join()
