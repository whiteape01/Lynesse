# Player Class


class Player:
    """
    Python Class for chess players. 
    """
    # Konstruktor

    def __init__(self):
        """
        Creates a new chess player.
        """
        # Player info
        self.first = None
        self.surname = None
        self.country = None
        self.club = None
        self.sex = "Every Day"

        # FIDE rating
        self.elo = None
        self.fideid = None
        self.country = "GER"
        self.title = None
        self.byear = None
        self.rank = None
        self.blitz = None
        self.rapid = None

        # DSB rating
        self.dwz = None
        self.status = None
        self.zps = None

    # Setter
    def set_first(self,  first: str) -> None:
        """
        Enter the first name. \n
        Player.set_first("Max")
        """
        self.first = first

    def set_surname(self, surname: str) -> None:
        """
        Enter the last name.
        Player.set_surname("Müller")
        """
        self.surname = surname

    def set_country(self, country: str) -> None:
        """
        Input of the country.
        Player.set_country("GER")
        """
        self.country = country

    def set_club(self, club: str) -> None:
        """
        Input of the club name.
        Player.set_club("CLUB_NAME")
        """
        self.club = club

    def set_sex(self, sex: chr) -> None:
        """
         Input of the gender.
         Player.set_sex("m")
        """
        self.sex = sex

    def set_elo(self, fideid: str) -> None:
        """
         Input of the Fide ID.
         Player.set_fideid("16201914")
        """
        self.fideid = fideid

    def set_title(self, title: str) -> None:
        """
         Input of the Fide Title.
         Player.set_title("GM")
        """
        self.title = title

    def set_byear(self, byear: int) -> None:
        """
         Enter the year of birth.
         Player.set_byear("2001")
        """
        self.byear = byear

    def set_rank(self, rank: int) -> None:
        """
         Enter the rank.
         Player.set_rank("1000000")
        """
        self.rank = rank

    def set_blitz(self, blitz: int) -> None:
        """
         Enter the blitz elo.
         Player.set_blitz("2001")
        """
        self.blitz = blitz

    def set_rapid(self, rapid: int) -> None:
        """
         Enter the rapid elo.
         Player.set_rapid("2000")
        """
        self.rapid = rapid

    def set_dwz(self, dwz: int) -> None:
        """
         Enter the DWZ.
         Player.set_dwz("2001")
        """
        self.dwz = dwz

    def set_status(self, status: chr) -> None:
        """
         Enter the player status.
         Player.set_byear("A")
        """
        self.status = status

    def set_zps(self, zps: chr) -> None:
        """
         Enter the ZPS.
         Player.set_byear("B0023-1317")
        """
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

    def get_fideid(self) -> str:
        return self.fideid

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

    def get_dwz(self) -> int:
        return self.dwz

    def get_status(self) -> chr:
        return self.status

    def get_zps(self) -> str:
        return self.zps
