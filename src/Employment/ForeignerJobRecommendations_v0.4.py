from enum import Enum
from typing import List, Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field, HttpUrl, constr

EscoCode = constr(pattern=r"^[0-9]{1,3}$|^[0-9]{4}(\.(?:([1-9]|[1-9][0-9]))){0,4}$")


class Industry(str, Enum):
    ICT = "ict"
    ENGINEERING = "engineering"
    ACADEMIC = "academic"
    HEALTH = "health"
    SALES = "sales"
    ADMINISTRATION = "administration"
    FINANCE = "finance"
    HR = "hr"
    MANUFACTURING = "manufacturing"
    MANAGEMENT = "management"
    GAMING = "gaming"


class FinnishMunicipality(str, Enum):
    AKAA = "020"
    ALAJARVI = "005"
    ALAVIESKA = "009"
    ALAVUS = "010"
    ASIKKALA = "016"
    ASKOLA = "018"
    AURA = "019"
    BRANDO = "035"
    ECKERO = "043"
    ENONKOSKI = "046"
    ENONTEKIO = "047"
    ESPOO = "049"
    EURA = "050"
    EURAJOKI = "051"
    EVIJARVI = "052"
    FINSTROM = "060"
    FORSSA = "061"
    FOGLO = "062"
    GETA = "065"
    HAAPAJARVI = "069"
    HAAPAVESI = "071"
    HAILUOTO = "072"
    HALSUA = "074"
    HAMINA = "075"
    HAMMARLAND = "076"
    HANKASALMI = "077"
    HANKO = "078"
    HARJAVALTA = "079"
    HARTOLA = "081"
    HATTULA = "082"
    HAUSJARVI = "086"
    HEINOLA = "111"
    HEINAVESI = "090"
    HELSINKI = "091"
    HIRVENSALMI = "097"
    HOLLOLA = "098"
    HUITTINEN = "102"
    HUMPPILA = "103"
    HYRYNSALMI = "105"
    HYVINKAA = "106"
    HAMEENKYRO = "108"
    HAMEENLINNA = "109"
    II = "139"
    IISALMI = "140"
    IITTI = "142"
    IKAALINEN = "143"
    ILMAJOKI = "145"
    ILOMANTSI = "146"
    IMATRA = "153"
    INARI = "148"
    INKOO = "149"
    ISOJOKI = "151"
    ISOKYRO = "152"
    JANAKKALA = "165"
    JOENSUU = "167"
    JOKIOINEN = "169"
    JOMALA = "170"
    JOROINEN = "171"
    JOUTSA = "172"
    JUUKA = "176"
    JUUPAJOKI = "177"
    JUVA = "178"
    JYVASKYLA = "179"
    JAMIJARVI = "181"
    JAMSA = "182"
    JARVENPAA = "186"
    KAARINA = "202"
    KAAVI = "204"
    KAJAANI = "205"
    KALAJOKI = "208"
    KANGASALA = "211"
    KANGASNIEMI = "213"
    KANKAANPAA = "214"
    KANNONKOSKI = "216"
    KANNUS = "217"
    KARIJOKI = "218"
    KARKKILA = "224"
    KARSTULA = "226"
    KARVIA = "230"
    KASKINEN = "231"
    KAUHAJOKI = "232"
    KAUHAVA = "233"
    KAUNIAINEN = "235"
    KAUSTINEN = "236"
    KEITELE = "239"
    KEMI = "240"
    KEMIJARVI = "320"
    KEMINMAA = "241"
    KEMIONSAARI = "322"
    KEMPELE = "244"
    KERAVA = "245"
    KEURUU = "249"
    KIHNIO = "250"
    KINNULA = "256"
    KIRKKONUMMI = "257"
    KITEE = "260"
    KITTILA = "261"
    KIURUVESI = "263"
    KIVIJARVI = "265"
    KOKEMAKI = "271"
    KOKKOLA = "272"
    KOLARI = "273"
    KONNEVESI = "275"
    KONTIOLAHTI = "276"
    KORSNAS = "280"
    KOSKI_TL = "284"
    KOTKA = "285"
    KOUVOLA = "286"
    KRISTIINANKAUPUNKI = "287"
    KRUUNUPYY = "288"
    KUHMO = "290"
    KUHMOINEN = "291"
    KUMLINGE = "295"
    KUOPIO = "297"
    KUORTANE = "300"
    KURIKKA = "301"
    KUSTAVI = "304"
    KUUSAMO = "305"
    KYYJARVI = "312"
    KARKOLA = "316"
    KARSAMAKI = "317"
    KOKAR = "318"
    LAHTI = "398"
    LAIHIA = "399"
    LAITILA = "400"
    LAPINJARVI = "407"
    LAPINLAHTI = "402"
    LAPPAJARVI = "403"
    LAPPEENRANTA = "405"
    LAPUA = "408"
    LAUKAA = "410"
    LEMI = "416"
    LEMLAND = "417"
    LEMPAALA = "418"
    LEPPAVIRTA = "420"
    LESTIJARVI = "421"
    LIEKSA = "422"
    LIETO = "423"
    LIMINKA = "425"
    LIPERI = "426"
    LOHJA = "444"
    LOIMAA = "430"
    LOPPI = "433"
    LOVIISA = "434"
    LUHANKA = "435"
    LUMIJOKI = "436"
    LUMPARLAND = "438"
    LUOTO = "440"
    LUUMAKI = "441"
    MAALAHTI = "475"
    MAARIANHAMINA = "478"
    MARTTILA = "480"
    MASKU = "481"
    MERIJARVI = "483"
    MERIKARVIA = "484"
    MIEHIKKALA = "489"
    MIKKELI = "491"
    MUHOS = "494"
    MULTIA = "495"
    MUONIO = "498"
    MUSTASAARI = "499"
    MUURAME = "500"
    MYNAMAKI = "503"
    MYRSKYLA = "504"
    MANTSALA = "505"
    MANTTA_VILPPULA = "508"
    MANTYHARJU = "507"
    NAANTALI = "529"
    NAKKILA = "531"
    NIVALA = "535"
    NOKIA = "536"
    NOUSIAINEN = "538"
    NURMES = "541"
    NURMIJARVI = "543"
    NARPIO = "545"
    ORIMATTILA = "560"
    ORIPAA = "561"
    ORIVESI = "562"
    OULAINEN = "563"
    OULU = "564"
    OUTOKUMPU = "309"
    PADASJOKI = "576"
    PAIMIO = "577"
    PALTAMO = "578"
    PARAINEN = "445"
    PARIKKALA = "580"
    PARKANO = "581"
    PEDERSOREN_KUNTA = "599"
    PELKOSENNIEMI = "583"
    PELLO = "854"
    PERHO = "584"
    PERTUNMAA = "588"
    PETAJAVESI = "592"
    PIEKSAMAKI = "593"
    PIELAVESI = "595"
    PIETARSAARI = "598"
    PIHTIPUDAS = "601"
    PIRKKALA = "604"
    POLVIJARVI = "607"
    POMARKKU = "608"
    PORI = "609"
    PORNAINEN = "611"
    PORVOO = "638"
    POSIO = "614"
    PUDASJARVI = "615"
    PUKKILA = "616"
    PUNKALAIDUN = "619"
    PUOLANKA = "620"
    PUUMALA = "623"
    PYHTAA = "624"
    PYHAJOKI = "625"
    PYHAJARVI = "626"
    PYHANTA = "630"
    PYHARANTA = "631"
    PALKANE = "635"
    POYTYA = "636"
    RAAHE = "678"
    RAASEPORI = "710"
    RAISIO = "680"
    RANTASALMI = "681"
    RANUA = "683"
    RAUMA = "684"
    RAUTALAMPI = "686"
    RAUTAVAARA = "687"
    RAUTJARVI = "689"
    REISJARVI = "691"
    RIIHIMAKI = "694"
    RISTIJARVI = "697"
    ROVANIEMI = "698"
    RUOKOLAHTI = "700"
    RUOVESI = "702"
    RUSKO = "704"
    RAAKKYLA = "707"
    SAARIJARVI = "729"
    SALLA = "732"
    SALO = "734"
    SALTVIK = "736"
    SASTAMALA = "790"
    SAUVO = "738"
    SAVITAIPALE = "739"
    SAVONLINNA = "740"
    SAVUKOSKI = "742"
    SEINAJOKI = "743"
    SIEVI = "746"
    SIIKAINEN = "747"
    SIIKAJOKI = "748"
    SIIKALATVA = "791"
    SIILINJARVI = "749"
    SIMO = "751"
    SIPOO = "753"
    SIUNTIO = "755"
    SODANKYLA = "758"
    SOINI = "759"
    SOMERO = "761"
    SONKAJARVI = "762"
    SOTKAMO = "765"
    SOTTUNGA = "766"
    SULKAVA = "768"
    SUND = "771"
    SUOMUSSALMI = "777"
    SUONENJOKI = "778"
    SYSMA = "781"
    SAKYLA = "783"
    TAIPALSAARI = "831"
    TAIVALKOSKI = "832"
    TAIVASSALO = "833"
    TAMMELA = "834"
    TAMPERE = "837"
    TERVO = "844"
    TERVOLA = "845"
    TEUVA = "846"
    TOHMAJARVI = "848"
    TOHOLAMPI = "849"
    TOIVAKKA = "850"
    TORNIO = "851"
    TURKU = "853"
    TUUSNIEMI = "857"
    TUUSULA = "858"
    TYRNAVA = "859"
    ULVILA = "886"
    URJALA = "887"
    UTAJARVI = "889"
    UTSJOKI = "890"
    UURAINEN = "892"
    UUSIKAARLEPYY = "893"
    UUSIKAUPUNKI = "895"
    VAALA = "785"
    VAASA = "905"
    VALKEAKOSKI = "908"
    VANTAA = "092"
    VARKAUS = "915"
    VEHMAA = "918"
    VESANTO = "921"
    VESILAHTI = "922"
    VETELI = "924"
    VIEREMA = "925"
    VIHTI = "927"
    VIITASAARI = "931"
    VIMPELI = "934"
    VIROLAHTI = "935"
    VIRRAT = "936"
    VARDO = "941"
    VOYRI = "946"
    YLITORNIO = "976"
    YLIVIESKA = "977"
    YLOJARVI = "980"
    YPAJA = "981"
    AHTARI = "989"
    AANEKOSKI = "992"


class CitizenshipArea(str, Enum):
    EEA = "EEA"
    NON_EEA = "non-EEA"


class ForeignerJobRecommendationsRequest(CamelCaseModel):
    esco_codes: Optional[List[EscoCode]] = Field(
        None,
        title="ESCO Codes",
        description="The ESCO code based on the standard ESCO occupation "
        "classification",
        examples=[["8331.1"]],
    )
    citizenship_area: Optional[CitizenshipArea] = Field(
        None,
        title="Citizenship Area",
        description="The citizenship area based on his or her native country. "
        "Switzerland is considered as part of the EEA category.",
        examples=[CitizenshipArea.EEA],
    )
    preferred_municipalities: Optional[List[FinnishMunicipality]] = Field(
        None,
        title="Preferred Municipalities",
        description="The potential municipalities in Finland that the user desires to "
        "find a job from.",
        examples=[[FinnishMunicipality.HELSINKI]],
    )
    industries: List[Industry] = Field(
        ...,
        title="Industries",
        description="The industry categories of the searched jobs",
        examples=[[Industry.ADMINISTRATION]],
    )
    free_text: Optional[str] = Field(
        None,
        title="Free Text",
        description="Free text that the user wants to use for filtering job "
        "advertisements",
        max_length=250,
        examples=["Driving license"],
    )
    limit: Optional[int] = Field(
        None,
        title="Limit",
        description="The limit of items per page in response",
        ge=1,
        examples=[1000],
    )
    offset: Optional[int] = Field(
        None,
        title="Offset",
        description="The starting index of responses",
        ge=0,
        examples=[0],
    )


class Employer(CamelCaseModel):
    name: str = Field(
        ...,
        title="Name",
        description="Then name of the employer issuing the job advertisement",
        max_length=250,
        examples=["Company Oy"],
    )
    logo_url: Optional[HttpUrl] = Field(
        None,
        alias="logoURL",
        title="Logo URL",
        description="The image URL of the employer logo",
        examples=["https://example.com/image.jpg"],
    )


class Job(CamelCaseModel):
    title: str = Field(
        ...,
        title="Title",
        description="Title of the advertised job",
        max_length=250,
        examples=["Item specialist"],
    )
    score: float = Field(
        ...,
        title="Score",
        description="The confidence score for the job advertisement recommendation",
        ge=0.0,
        le=1.0,
        examples=[0.88],
    )
    industries: List[Industry] = Field(
        ...,
        title="Industries",
        description="The industry categories of the advertised job",
        examples=[[Industry.ADMINISTRATION]],
    )
    advertisement_url: HttpUrl = Field(
        ...,
        alias="advertisementURL",
        title="Advertisement URL",
        description="The link to the service providing the job advertisement details",
        examples=["https://jobadvertisement.example.com/ad123"],
    )
    municipality_code: Optional[FinnishMunicipality] = Field(
        None,
        title="Municipality Code",
        description="The location of the advertised job",
        examples=[FinnishMunicipality.HELSINKI],
    )
    employer: Employer = Field(
        ...,
        title="Employer",
        description="The details of an employer that issued the job advertisement",
    )


class ForeignerJobRecommendationsResponse(CamelCaseModel):
    identifier: str = Field(
        ...,
        title="Identifier",
        description="The job recommendation search identifier",
        examples=["123e4567-e89b-12d3-a456-426614174000"],
    )
    jobs: List[Job] = Field(
        ...,
        title="Jobs",
        description="The list of jobs recommended for the foreigner based on the input "
        "properties. In case of no input filters this field will have an empty list "
        "and the total jobs field will show the total count.",
    )
    total_jobs: int = Field(
        ...,
        title="Total Jobs",
        description="The total count of job recommendations",
        examples=[47],
    )


DEFINITION = DataProductDefinition(
    version="0.4.1",
    strict_validation=False,
    title="Foreigner Job Recommendations",
    description="Returns the list of jobs recommended for the foreigner based on e.g. "
    "the citizenship area and previous occupations based on the European Standard "
    "Classification of Occupations (ESCO) version 1.1.1",
    request=ForeignerJobRecommendationsRequest,
    response=ForeignerJobRecommendationsResponse,
    requires_authorization=False,
    requires_consent=False,
)
