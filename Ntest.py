from Nvminit import mount_img_solaris

imgpath = "/build/solaris.img"
mntpath = "/mnt/tmp"
device = "/dev/loop0"
mount_img_solaris(imgpath, mntpath, device)
