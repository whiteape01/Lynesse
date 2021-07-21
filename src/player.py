# Player Class

class player:
    # Konstruktor
    def __init__(self):
        # Player info
        self.first = None
        self.surname = None
        self.country = None
        self.club = None
        self.sex = "Every Day"

        # FIDE rating
        self.elo = None
        self.fide_id = None
        self.country = "GER"
        self.title = None
        self.byear = None
        self.rank = None
        self.blitz = None
        self.rapid = None

        # DSB rating
        self.dsb_id = None
        self.dwz = None
        self.status = None
        self.zps = None

    # Setter
    def set_first(self,  first: str) -> None:
        self.first = first

    def set_surname(self, surname) -> None:
        self.surname = surname

    def set_country(self, country) -> None:
        self.country = country

    def set_club(self, club) -> None:
        self.club = club

    def set_sex(self, sex) -> None:
        self.sex = sex

    def set_sex(self, elo) -> None:
        self.sex = elo

    def set_elo(self, fideid) -> None:
        self.fideid = fideid

    def set_country(self, country) -> None:
        self.country = country

    def set_title(self, title) -> None:
        self.title = title

    def set_byear(self, byear) -> None:
        self.byear = byear

    def set_rank(self, rank) -> None:
        self.rank = rank

    def set_blitz(self, blitz) -> None:
        self.blitz = blitz

    def set_rapid(self, rapid) -> None:
        self.rapid = rapid

    def set_dsbid(self, dsb_id) -> None:
        self.dsbid = dsb_id

    def set_dwz(self, dwz) -> None:
        self.dwz = dwz

    def set_status(self, status) -> None:
        self.status = status

    def set_zps(self, zps) -> None:
        self.zps = zps

    # Getter
    def get_first(self) -> str:
        return self.first

    def get_surname(self) -> str:
        return self.surname

    def get_country(self) -> str:
        return self.country

    def get_club(self) -> str:
        return self.club

    def get_sex(self) -> chr:
        return self.sex

    def get_elo(self) -> int:
        return self.elo

    def get_fide_id(self) -> str:
        return self.fide_id

    def get_country(self) -> int:
        return self.country

    def get_title(self) -> str:
        return self.title

    def get_byear(self) -> int:
        return self.byear

    def get_rank(self) -> int:
        return self.rank

    def get_blitz(self) -> int:
        return self.blitz

    def get_rapid(self) -> int:
        return self.rapid

    def get_dsbid(self) -> str:
        return self.dsbid

    def get_dwz(self) -> int:
        return self.dwz

    def get_status(self) -> chr:
        return self.status

    def get_zps(self) -> str:
        return self.zps
