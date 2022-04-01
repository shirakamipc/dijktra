import math
from xml.sax.saxutils import prepare_input_source
def tao_do_thi_co_huong_tu_tap_tin():
    f = open('do_thi_co_huong.txt')
    so_luong_dinh = int(f.readline().strip())
    cac_dong = f.readlines()
    f.close()
    
    do_thi = [[0 for _ in range(so_luong_dinh)] for _ in range(so_luong_dinh)]
    
    for dong in cac_dong:
        ds_gia_tri = dong.split()
        if len(ds_gia_tri) != 3:
            continue
        else:
            dong = int(ds_gia_tri[0])
            cot = int(ds_gia_tri[1])
            khoang_cach = int(ds_gia_tri[2])
            do_thi[dong][cot] = khoang_cach
        
    return do_thi

def lay_duong_di(ds_dinh_truoc, dinh_dich):
    ds_dinh_di_qua = [dinh_dich]
    dinh = dinh_dich
    while True:
        dinh = ds_dinh_truoc[dinh]
        if dinh == None:
            break
        else:
            ds_dinh_di_qua.insert(0, dinh)
    
    ds_dinh_di_qua = [str(x) for x in ds_dinh_di_qua]
    return '->'.join(ds_dinh_di_qua)

def khoang_cach_ngan_nhat(ds_khoang_cach, ds_dinh_cay_ngan_nhat):
    nho_nhat = math.inf
    dinh_nho_nhat = math.inf
    for dinh in range(len(ds_khoang_cach)):
        if ds_dinh_cay_ngan_nhat[dinh] == False and ds_khoang_cach[dinh] < nho_nhat:
            nho_nhat = ds_khoang_cach[dinh]
            dinh_nho_nhat = dinh
    
    return dinh_nho_nhat

def dijkstra(do_thi, dinh_nguon, dinh_dich):
    so_luong_dinh = len(do_thi)
    
    ds_khoang_cach = [math.inf for _ in range(so_luong_dinh)]
    ds_khoang_cach[dinh_nguon] = 0
    ds_dinh_truoc = [None for _ in range(so_luong_dinh)]
    
    ds_dinh_cay_ngan_nhat = [False for _ in range(so_luong_dinh)]
    
    for i in range(so_luong_dinh):
        x = khoang_cach_ngan_nhat(ds_khoang_cach, ds_dinh_cay_ngan_nhat)
        
        if x == math.inf:
            print(f'Khong co duong di tu dinh {dinh_nguon} den dinh {dinh_dich}')
            return
        ds_dinh_cay_ngan_nhat[x] = True
        if x == dinh_dich:
            print(f'Tim thay duong di tu dinh {dinh_nguon} den dinh {dinh_dich}')
            duong_di = lay_duong_di(ds_dinh_truoc, dinh_dich)
            thong_bao = f'Tu dinh {dinh_nguon} den dinh {dinh_dich} : ' + duong_di + ' : ' + str(ds_khoang_cach[dinh_dich])
            print(thong_bao)
            return
        else:
            for y in range(so_luong_dinh):
                if ds_dinh_cay_ngan_nhat[y] == False and do_thi[x][y] > 0 and ds_khoang_cach[y] > ds_khoang_cach[x] + do_thi[x][y]:
                    ds_khoang_cach[y] = ds_khoang_cach[x] + do_thi[x][y]
                    ds_dinh_truoc[y] = x
def main():
    do_thi = tao_do_thi_co_huong_tu_tap_tin()
    so_luong_dinh = len(do_thi)
    print('So luong dinh', so_luong_dinh)
    dinh_nguon = int(input('Nhap vao dinh nguon: '))
    dinh_dich = int(input('Nhap dinh dinh dich: '))
    if dinh_nguon in range(so_luong_dinh) and dinh_dich in range(so_luong_dinh):
        dijkstra(do_thi, dinh_nguon, dinh_dich)
    
if __name__ == '__main__':
    main()                     
                    