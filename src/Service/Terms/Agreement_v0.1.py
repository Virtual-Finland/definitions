from datetime import datetime
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field, HttpUrl


class AgreementRequest(CamelCaseModel):
    pass


class CurrentTerms(CamelCaseModel):
    url: HttpUrl = Field(
        ...,
        title="Terms of service URL",
        description="URL to the terms of service contents.",
        example="https://example.com/terms-of-service-v1.0",
    )
    description: str = Field(
        ...,
        title="Description",
        description="Description of the terms of service",
        example="This is the terms of service for the example service.",
    )
    version: str = Field(
        ...,
        title="Version",
        description="Version of the terms of service.",
        example="1.0",
    )


class AgreementResponse(CamelCaseModel):
    current_terms: CurrentTerms = Field(
        ...,
        title="Current terms",
        description="The current terms of service.",
    )
    accepted_version: str = Field(
        ...,
        title="Accepted version",
        description="The version the service user has accepted. If the service user has not accepted any version of the terms of service, this field is null.",
        example=False,
        nullable=True,
    )
    accepted_at: Optional[datetime] = Field(
        None,
        title="Accepted at",
        description="When the terms of service was accepted in RFC3339 date-time format. If the service user has not accepted any version of the terms of service, this field is null.",
        example="2023-09-13T11:52:00Z",
        nullable=True,
    )
    has_accepted_latest: bool = Field(
        ...,
        title="Has accepted the latest version",
        description="Whether the service user has accepted the latest version of the terms of service.",
        example=False,
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Terms of Service Agreement",
    description="The current terms of service and the service user's agreement to them.",
    request=AgreementRequest,
    response=AgreementResponse,
    requires_authorization=True,
)
