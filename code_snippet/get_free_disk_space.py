import os
import ctypes
import sys

def get_machine_free_disk_size():
    '''
    return free disk size of machine in MB
    '''
    
    if 'win' != sys.platform[:3]:
        # cmd = "python -c \"import os;print (os.statvfs('/').f_bavail*os.statvfs('/').f_frsize)/1024/1024\""
        return (os.statvfs('/').f_bavail*os.statvfs('/').f_frsize)/1024/1024
    else:
        # cmd = "python -c \"import ctypes,os;free_bytes = ctypes.c_ulonglong(0);ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p('/'),None, None, ctypes.pointer(free_bytes));print free_bytes.value/1024/1024\""
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p('/'),None, None, ctypes.pointer(free_bytes))
        return free_bytes.value/1024/1024


if __name__ == '__main__':
    free_size = get_machine_free_disk_size()
    print free_size