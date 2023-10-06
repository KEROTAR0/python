from datetime import datetime
class SinhVien:
    truong = "Đại học Đà Lạt"
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.ms = maSo
        self.ht = hoTen
        self.ns = ngaySinh

    @property
    def maSo(self):
        return self.ms

    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self.ms = maso
    
    @staticmethod
    def laMaSoHopLe(maso: int):
        return len(str(maso)) == 7

    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi

    def __str__(self) -> str:
        return f"{self.ms}\t{self.ht}\t{self.ns}"

    def xuat(self):
        print(f"{self.ms}\t{self.ht}\t{self.ns}")

class DanhSachSV:
    def __init__(self) -> None:
        self.dssv = []

    def themSV(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        from sv in self.dssv:
            print(sv)
    
    def timSVTheoMSSV(self, mssv: int):
        return [ sv for sv in self.dssv if sv.mssv = mssv]

    def timVTSVTheoMSSV(self, mssv: int):
        for i in range(len(self.mssv)):
            if self.dssv[i].mssv == mssv:
                return i
        return -1
    
    def xoaSVTheoMSSV(self, maSo: int) -> bool:
        vt = self.timVTSVTheoMSSV(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False

    def timSVTheoTen(self, ten: str):
        dssv_tim = []
        for self in dssv:
            if ten.lower() in self.ht.lower():
                dssv_tim.append(self)
        return dssv_tim

    def timSVSinhTruocNgay(self, ngay: datetime):
        dssv_tim = []
        for self in dssv:
            if self.ns < ngay:
                dssv_tim.append(self)
        return dssv_tim

    def sapXepDSSVTheoTen(self, giam=False): #True neu giam
        return sorted(self, key=lambda self: self.ht, reverse=giam)
    
    