from datetime import date
from enum import Enum
from typing import List, Optional

from converter import CamelCaseModel, DataProductDefinition
from pydantic import EmailStr, Field, constr


class ISO_3166_1_Alpha_3(str, Enum):
    AFG = "AFG"
    ALB = "ALB"
    DZA = "DZA"
    ASM = "ASM"
    AND = "AND"
    AGO = "AGO"
    AIA = "AIA"
    ATA = "ATA"
    ATG = "ATG"
    ARG = "ARG"
    ARM = "ARM"
    ABW = "ABW"
    AUS = "AUS"
    AUT = "AUT"
    AZE = "AZE"
    BHS = "BHS"
    BHR = "BHR"
    BGD = "BGD"
    BRB = "BRB"
    BLR = "BLR"
    BEL = "BEL"
    BLZ = "BLZ"
    BEN = "BEN"
    BMU = "BMU"
    BTN = "BTN"
    BOL = "BOL"
    BIH = "BIH"
    BWA = "BWA"
    BVT = "BVT"
    BRA = "BRA"
    IOT = "IOT"
    BRN = "BRN"
    BGR = "BGR"
    BFA = "BFA"
    BDI = "BDI"
    KHM = "KHM"
    CMR = "CMR"
    CAN = "CAN"
    CPV = "CPV"
    CYM = "CYM"
    CAF = "CAF"
    TCD = "TCD"
    CHL = "CHL"
    CHN = "CHN"
    CXR = "CXR"
    CCK = "CCK"
    COL = "COL"
    COM = "COM"
    COG = "COG"
    COD = "COD"
    COK = "COK"
    CRI = "CRI"
    CIV = "CIV"
    HRV = "HRV"
    CUB = "CUB"
    CYP = "CYP"
    CZE = "CZE"
    DNK = "DNK"
    DJI = "DJI"
    DMA = "DMA"
    DOM = "DOM"
    ECU = "ECU"
    EGY = "EGY"
    SLV = "SLV"
    GNQ = "GNQ"
    ERI = "ERI"
    EST = "EST"
    ETH = "ETH"
    FLK = "FLK"
    FRO = "FRO"
    FJI = "FJI"
    FIN = "FIN"
    FRA = "FRA"
    GUF = "GUF"
    PYF = "PYF"
    ATF = "ATF"
    GAB = "GAB"
    GMB = "GMB"
    GEO = "GEO"
    DEU = "DEU"
    GHA = "GHA"
    GIB = "GIB"
    GRC = "GRC"
    GRL = "GRL"
    GRD = "GRD"
    GLP = "GLP"
    GUM = "GUM"
    GTM = "GTM"
    GGY = "GGY"
    GIN = "GIN"
    GNB = "GNB"
    GUY = "GUY"
    HTI = "HTI"
    HMD = "HMD"
    VAT = "VAT"
    HND = "HND"
    HKG = "HKG"
    HUN = "HUN"
    ISL = "ISL"
    IND = "IND"
    IDN = "IDN"
    IRN = "IRN"
    IRQ = "IRQ"
    IRL = "IRL"
    IMN = "IMN"
    ISR = "ISR"
    ITA = "ITA"
    JAM = "JAM"
    JPN = "JPN"
    JEY = "JEY"
    JOR = "JOR"
    KAZ = "KAZ"
    KEN = "KEN"
    KIR = "KIR"
    PRK = "PRK"
    KOR = "KOR"
    KWT = "KWT"
    KGZ = "KGZ"
    LAO = "LAO"
    LVA = "LVA"
    LBN = "LBN"
    LSO = "LSO"
    LBR = "LBR"
    LBY = "LBY"
    LIE = "LIE"
    LTU = "LTU"
    LUX = "LUX"
    MAC = "MAC"
    MKD = "MKD"
    MDG = "MDG"
    MWI = "MWI"
    MYS = "MYS"
    MDV = "MDV"
    MLI = "MLI"
    MLT = "MLT"
    MHL = "MHL"
    MTQ = "MTQ"
    MRT = "MRT"
    MUS = "MUS"
    MYT = "MYT"
    MEX = "MEX"
    FSM = "FSM"
    MDA = "MDA"
    MCO = "MCO"
    MNG = "MNG"
    MNE = "MNE"
    MSR = "MSR"
    MAR = "MAR"
    MOZ = "MOZ"
    MMR = "MMR"
    NAM = "NAM"
    NRU = "NRU"
    NPL = "NPL"
    NLD = "NLD"
    ANT = "ANT"
    NCL = "NCL"
    NZL = "NZL"
    NIC = "NIC"
    NER = "NER"
    NGA = "NGA"
    NIU = "NIU"
    NFK = "NFK"
    MNP = "MNP"
    NOR = "NOR"
    OMN = "OMN"
    PAK = "PAK"
    PLW = "PLW"
    PSE = "PSE"
    PAN = "PAN"
    PNG = "PNG"
    PRY = "PRY"
    PER = "PER"
    PHL = "PHL"
    PCN = "PCN"
    POL = "POL"
    PRT = "PRT"
    PRI = "PRI"
    QAT = "QAT"
    REU = "REU"
    ROU = "ROU"
    RUS = "RUS"
    RWA = "RWA"
    SHN = "SHN"
    KNA = "KNA"
    LCA = "LCA"
    SPM = "SPM"
    VCT = "VCT"
    WSM = "WSM"
    SMR = "SMR"
    STP = "STP"
    SAU = "SAU"
    SEN = "SEN"
    SRB = "SRB"
    SYC = "SYC"
    SLE = "SLE"
    SGP = "SGP"
    SVK = "SVK"
    SVN = "SVN"
    SLB = "SLB"
    SOM = "SOM"
    ZAF = "ZAF"
    SGS = "SGS"
    SSD = "SSD"
    ESP = "ESP"
    LKA = "LKA"
    SDN = "SDN"
    SUR = "SUR"
    SJM = "SJM"
    SWZ = "SWZ"
    SWE = "SWE"
    CHE = "CHE"
    SYR = "SYR"
    TWN = "TWN"
    TJK = "TJK"
    TZA = "TZA"
    THA = "THA"
    TLS = "TLS"
    TGO = "TGO"
    TKL = "TKL"
    TON = "TON"
    TTO = "TTO"
    TUN = "TUN"
    TUR = "TUR"
    TKM = "TKM"
    TCA = "TCA"
    TUV = "TUV"
    UGA = "UGA"
    UKR = "UKR"
    ARE = "ARE"
    GBR = "GBR"
    USA = "USA"
    UMI = "UMI"
    URY = "URY"
    UZB = "UZB"
    VUT = "VUT"
    VEN = "VEN"
    VNM = "VNM"
    VGB = "VGB"
    VIR = "VIR"
    WLF = "WLF"
    ESH = "ESH"
    YEM = "YEM"
    ZMB = "ZMB"
    ZWE = "ZWE"


class BasicInformationRequestResponse(CamelCaseModel):
    given_name: str = Field(
        None,
        title="Given name",
        description="The first name that the person is being called by",
        example="John",
        max_length=250,
    )
    last_name: str = Field(
        None,
        title="Last name",
        description="The person's current family name",
        example="Doe",
        max_length=250,
    )
    email: EmailStr = Field(
        ...,
        title="Email",
        description="The person's contact email address",
        example="john.doe@test.fi",
    )
    phone_number: str = Field(
        None,
        title="Phone number",
        description="The person's phone number in the international format",
        example="+358501234567",
        max_length=250,
    )
    residency: ISO_3166_1_Alpha_3 = Field(
        ...,
        title="Residency",
        description="The person's current country of the residency in the three character (Alpha-3) format",
        example=[ISO_3166_1_Alpha_3.USA],
    )


DEFINITION = DataProductDefinition(
    description="Create or update a minimal set of basic information of a person",
    request=BasicInformationRequestResponse,
    response=BasicInformationRequestResponse,
    summary="Write Person Basic Information",
    requires_authorization=True,
    requires_consent=True,
)
