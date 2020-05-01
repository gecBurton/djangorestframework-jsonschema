from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from . import serializers, models, filters


class Element(viewsets.ModelViewSet):
    queryset = models.Element.objects.all()
    serializer_class = serializers.Element
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Element
    ordering_fields = "__all__"


class Extension(viewsets.ModelViewSet):
    queryset = models.Extension.objects.all()
    serializer_class = serializers.Extension
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Extension
    ordering_fields = "__all__"
    search_fields = [
        "$valueBase64Binary",
        "$valueCanonical",
        "$valueCode",
        "$valueDate",
        "$valueDateTime",
        "$valueId",
        "$valueInstant",
        "$valueMarkdown",
        "$valueOid",
        "$valueString",
        "$valueTime",
        "$valueUri",
        "$valueUrl",
        "$valueUuid",
    ]


class Narrative(viewsets.ModelViewSet):
    queryset = models.Narrative.objects.all()
    serializer_class = serializers.Narrative
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Narrative
    ordering_fields = "__all__"


class Annotation(viewsets.ModelViewSet):
    queryset = models.Annotation.objects.all()
    serializer_class = serializers.Annotation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Annotation
    ordering_fields = "__all__"
    search_fields = [
        "$authorString",
    ]


class Attachment(viewsets.ModelViewSet):
    queryset = models.Attachment.objects.all()
    serializer_class = serializers.Attachment
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Attachment
    ordering_fields = "__all__"


class Identifier(viewsets.ModelViewSet):
    queryset = models.Identifier.objects.all()
    serializer_class = serializers.Identifier
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Identifier
    ordering_fields = "__all__"


class CodeableConcept(viewsets.ModelViewSet):
    queryset = models.CodeableConcept.objects.all()
    serializer_class = serializers.CodeableConcept
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CodeableConcept
    ordering_fields = "__all__"


class Coding(viewsets.ModelViewSet):
    queryset = models.Coding.objects.all()
    serializer_class = serializers.Coding
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Coding
    ordering_fields = "__all__"


class Quantity(viewsets.ModelViewSet):
    queryset = models.Quantity.objects.all()
    serializer_class = serializers.Quantity
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Quantity
    ordering_fields = "__all__"


class Duration(viewsets.ModelViewSet):
    queryset = models.Duration.objects.all()
    serializer_class = serializers.Duration
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Duration
    ordering_fields = "__all__"


class Distance(viewsets.ModelViewSet):
    queryset = models.Distance.objects.all()
    serializer_class = serializers.Distance
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Distance
    ordering_fields = "__all__"


class Count(viewsets.ModelViewSet):
    queryset = models.Count.objects.all()
    serializer_class = serializers.Count
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Count
    ordering_fields = "__all__"


class Money(viewsets.ModelViewSet):
    queryset = models.Money.objects.all()
    serializer_class = serializers.Money
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Money
    ordering_fields = "__all__"


class Age(viewsets.ModelViewSet):
    queryset = models.Age.objects.all()
    serializer_class = serializers.Age
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Age
    ordering_fields = "__all__"


class Range(viewsets.ModelViewSet):
    queryset = models.Range.objects.all()
    serializer_class = serializers.Range
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Range
    ordering_fields = "__all__"


class Period(viewsets.ModelViewSet):
    queryset = models.Period.objects.all()
    serializer_class = serializers.Period
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Period
    ordering_fields = "__all__"


class Ratio(viewsets.ModelViewSet):
    queryset = models.Ratio.objects.all()
    serializer_class = serializers.Ratio
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Ratio
    ordering_fields = "__all__"


class Reference(viewsets.ModelViewSet):
    queryset = models.Reference.objects.all()
    serializer_class = serializers.Reference
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Reference
    ordering_fields = "__all__"


class SampledData(viewsets.ModelViewSet):
    queryset = models.SampledData.objects.all()
    serializer_class = serializers.SampledData
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SampledData
    ordering_fields = "__all__"


class Signature(viewsets.ModelViewSet):
    queryset = models.Signature.objects.all()
    serializer_class = serializers.Signature
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Signature
    ordering_fields = "__all__"


class HumanName(viewsets.ModelViewSet):
    queryset = models.HumanName.objects.all()
    serializer_class = serializers.HumanName
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.HumanName
    ordering_fields = "__all__"


class Address(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.Address
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Address
    ordering_fields = "__all__"


class ContactPoint(viewsets.ModelViewSet):
    queryset = models.ContactPoint.objects.all()
    serializer_class = serializers.ContactPoint
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ContactPoint
    ordering_fields = "__all__"


class Timing(viewsets.ModelViewSet):
    queryset = models.Timing.objects.all()
    serializer_class = serializers.Timing
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Timing
    ordering_fields = "__all__"


class Timing_Repeat(viewsets.ModelViewSet):
    queryset = models.Timing_Repeat.objects.all()
    serializer_class = serializers.Timing_Repeat
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Timing_Repeat
    ordering_fields = "__all__"


class Meta(viewsets.ModelViewSet):
    queryset = models.Meta.objects.all()
    serializer_class = serializers.Meta
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Meta
    ordering_fields = "__all__"


class ContactDetail(viewsets.ModelViewSet):
    queryset = models.ContactDetail.objects.all()
    serializer_class = serializers.ContactDetail
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ContactDetail
    ordering_fields = "__all__"


class Contributor(viewsets.ModelViewSet):
    queryset = models.Contributor.objects.all()
    serializer_class = serializers.Contributor
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Contributor
    ordering_fields = "__all__"


class DataRequirement(viewsets.ModelViewSet):
    queryset = models.DataRequirement.objects.all()
    serializer_class = serializers.DataRequirement
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DataRequirement
    ordering_fields = "__all__"


class DataRequirement_CodeFilter(viewsets.ModelViewSet):
    queryset = models.DataRequirement_CodeFilter.objects.all()
    serializer_class = serializers.DataRequirement_CodeFilter
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DataRequirement_CodeFilter
    ordering_fields = "__all__"


class DataRequirement_DateFilter(viewsets.ModelViewSet):
    queryset = models.DataRequirement_DateFilter.objects.all()
    serializer_class = serializers.DataRequirement_DateFilter
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DataRequirement_DateFilter
    ordering_fields = "__all__"
    search_fields = [
        "$valueDateTime",
    ]


class DataRequirement_Sort(viewsets.ModelViewSet):
    queryset = models.DataRequirement_Sort.objects.all()
    serializer_class = serializers.DataRequirement_Sort
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DataRequirement_Sort
    ordering_fields = "__all__"


class ParameterDefinition(viewsets.ModelViewSet):
    queryset = models.ParameterDefinition.objects.all()
    serializer_class = serializers.ParameterDefinition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ParameterDefinition
    ordering_fields = "__all__"


class RelatedArtifact(viewsets.ModelViewSet):
    queryset = models.RelatedArtifact.objects.all()
    serializer_class = serializers.RelatedArtifact
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.RelatedArtifact
    ordering_fields = "__all__"


class TriggerDefinition(viewsets.ModelViewSet):
    queryset = models.TriggerDefinition.objects.all()
    serializer_class = serializers.TriggerDefinition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TriggerDefinition
    ordering_fields = "__all__"
    search_fields = [
        "$timingDate",
        "$timingDateTime",
    ]


class UsageContext(viewsets.ModelViewSet):
    queryset = models.UsageContext.objects.all()
    serializer_class = serializers.UsageContext
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.UsageContext
    ordering_fields = "__all__"


class Dosage(viewsets.ModelViewSet):
    queryset = models.Dosage.objects.all()
    serializer_class = serializers.Dosage
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Dosage
    ordering_fields = "__all__"


class Dosage_DoseAndRate(viewsets.ModelViewSet):
    queryset = models.Dosage_DoseAndRate.objects.all()
    serializer_class = serializers.Dosage_DoseAndRate
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Dosage_DoseAndRate
    ordering_fields = "__all__"


class Population(viewsets.ModelViewSet):
    queryset = models.Population.objects.all()
    serializer_class = serializers.Population
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Population
    ordering_fields = "__all__"


class ProductShelfLife(viewsets.ModelViewSet):
    queryset = models.ProductShelfLife.objects.all()
    serializer_class = serializers.ProductShelfLife
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ProductShelfLife
    ordering_fields = "__all__"


class ProdCharacteristic(viewsets.ModelViewSet):
    queryset = models.ProdCharacteristic.objects.all()
    serializer_class = serializers.ProdCharacteristic
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ProdCharacteristic
    ordering_fields = "__all__"


class MarketingStatus(viewsets.ModelViewSet):
    queryset = models.MarketingStatus.objects.all()
    serializer_class = serializers.MarketingStatus
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MarketingStatus
    ordering_fields = "__all__"


class SubstanceAmount(viewsets.ModelViewSet):
    queryset = models.SubstanceAmount.objects.all()
    serializer_class = serializers.SubstanceAmount
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceAmount
    ordering_fields = "__all__"
    search_fields = [
        "$amountString",
    ]


class SubstanceAmount_ReferenceRange(viewsets.ModelViewSet):
    queryset = models.SubstanceAmount_ReferenceRange.objects.all()
    serializer_class = serializers.SubstanceAmount_ReferenceRange
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceAmount_ReferenceRange
    ordering_fields = "__all__"


class Expression(viewsets.ModelViewSet):
    queryset = models.Expression.objects.all()
    serializer_class = serializers.Expression
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Expression
    ordering_fields = "__all__"


class ElementDefinition(viewsets.ModelViewSet):
    queryset = models.ElementDefinition.objects.all()
    serializer_class = serializers.ElementDefinition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ElementDefinition
    ordering_fields = "__all__"
    search_fields = [
        "$defaultValueBase64Binary",
        "$defaultValueCanonical",
        "$defaultValueCode",
        "$defaultValueDate",
        "$defaultValueDateTime",
        "$defaultValueId",
        "$defaultValueInstant",
        "$defaultValueMarkdown",
        "$defaultValueOid",
        "$defaultValueString",
        "$defaultValueTime",
        "$defaultValueUri",
        "$defaultValueUrl",
        "$defaultValueUuid",
        "$fixedBase64Binary",
        "$fixedCanonical",
        "$fixedCode",
        "$fixedDate",
        "$fixedDateTime",
        "$fixedId",
        "$fixedInstant",
        "$fixedMarkdown",
        "$fixedOid",
        "$fixedString",
        "$fixedTime",
        "$fixedUri",
        "$fixedUrl",
        "$fixedUuid",
        "$patternBase64Binary",
        "$patternCanonical",
        "$patternCode",
        "$patternDate",
        "$patternDateTime",
        "$patternId",
        "$patternInstant",
        "$patternMarkdown",
        "$patternOid",
        "$patternString",
        "$patternTime",
        "$patternUri",
        "$patternUrl",
        "$patternUuid",
        "$minValueDate",
        "$minValueDateTime",
        "$minValueInstant",
        "$minValueTime",
        "$maxValueDate",
        "$maxValueDateTime",
        "$maxValueInstant",
        "$maxValueTime",
    ]


class ElementDefinition_Slicing(viewsets.ModelViewSet):
    queryset = models.ElementDefinition_Slicing.objects.all()
    serializer_class = serializers.ElementDefinition_Slicing
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ElementDefinition_Slicing
    ordering_fields = "__all__"


class ElementDefinition_Discriminator(viewsets.ModelViewSet):
    queryset = models.ElementDefinition_Discriminator.objects.all()
    serializer_class = serializers.ElementDefinition_Discriminator
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ElementDefinition_Discriminator
    ordering_fields = "__all__"


class ElementDefinition_Base(viewsets.ModelViewSet):
    queryset = models.ElementDefinition_Base.objects.all()
    serializer_class = serializers.ElementDefinition_Base
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ElementDefinition_Base
    ordering_fields = "__all__"


class ElementDefinition_Type(viewsets.ModelViewSet):
    queryset = models.ElementDefinition_Type.objects.all()
    serializer_class = serializers.ElementDefinition_Type
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ElementDefinition_Type
    ordering_fields = "__all__"


class ElementDefinition_Example(viewsets.ModelViewSet):
    queryset = models.ElementDefinition_Example.objects.all()
    serializer_class = serializers.ElementDefinition_Example
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ElementDefinition_Example
    ordering_fields = "__all__"
    search_fields = [
        "$valueBase64Binary",
        "$valueCanonical",
        "$valueCode",
        "$valueDate",
        "$valueDateTime",
        "$valueId",
        "$valueInstant",
        "$valueMarkdown",
        "$valueOid",
        "$valueString",
        "$valueTime",
        "$valueUri",
        "$valueUrl",
        "$valueUuid",
    ]


class ElementDefinition_Constraint(viewsets.ModelViewSet):
    queryset = models.ElementDefinition_Constraint.objects.all()
    serializer_class = serializers.ElementDefinition_Constraint
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ElementDefinition_Constraint
    ordering_fields = "__all__"


class ElementDefinition_Binding(viewsets.ModelViewSet):
    queryset = models.ElementDefinition_Binding.objects.all()
    serializer_class = serializers.ElementDefinition_Binding
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ElementDefinition_Binding
    ordering_fields = "__all__"


class ElementDefinition_Mapping(viewsets.ModelViewSet):
    queryset = models.ElementDefinition_Mapping.objects.all()
    serializer_class = serializers.ElementDefinition_Mapping
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ElementDefinition_Mapping
    ordering_fields = "__all__"


class Account(viewsets.ModelViewSet):
    queryset = models.Account.objects.all()
    serializer_class = serializers.Account
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Account
    ordering_fields = "__all__"


class Account_Coverage(viewsets.ModelViewSet):
    queryset = models.Account_Coverage.objects.all()
    serializer_class = serializers.Account_Coverage
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Account_Coverage
    ordering_fields = "__all__"


class Account_Guarantor(viewsets.ModelViewSet):
    queryset = models.Account_Guarantor.objects.all()
    serializer_class = serializers.Account_Guarantor
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Account_Guarantor
    ordering_fields = "__all__"


class ActivityDefinition(viewsets.ModelViewSet):
    queryset = models.ActivityDefinition.objects.all()
    serializer_class = serializers.ActivityDefinition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ActivityDefinition
    ordering_fields = "__all__"
    search_fields = [
        "$timingDateTime",
    ]


class ActivityDefinition_Participant(viewsets.ModelViewSet):
    queryset = models.ActivityDefinition_Participant.objects.all()
    serializer_class = serializers.ActivityDefinition_Participant
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ActivityDefinition_Participant
    ordering_fields = "__all__"


class ActivityDefinition_DynamicValue(viewsets.ModelViewSet):
    queryset = models.ActivityDefinition_DynamicValue.objects.all()
    serializer_class = serializers.ActivityDefinition_DynamicValue
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ActivityDefinition_DynamicValue
    ordering_fields = "__all__"


class AdverseEvent(viewsets.ModelViewSet):
    queryset = models.AdverseEvent.objects.all()
    serializer_class = serializers.AdverseEvent
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.AdverseEvent
    ordering_fields = "__all__"


class AdverseEvent_SuspectEntity(viewsets.ModelViewSet):
    queryset = models.AdverseEvent_SuspectEntity.objects.all()
    serializer_class = serializers.AdverseEvent_SuspectEntity
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.AdverseEvent_SuspectEntity
    ordering_fields = "__all__"


class AdverseEvent_Causality(viewsets.ModelViewSet):
    queryset = models.AdverseEvent_Causality.objects.all()
    serializer_class = serializers.AdverseEvent_Causality
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.AdverseEvent_Causality
    ordering_fields = "__all__"


class AllergyIntolerance(viewsets.ModelViewSet):
    queryset = models.AllergyIntolerance.objects.all()
    serializer_class = serializers.AllergyIntolerance
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.AllergyIntolerance
    ordering_fields = "__all__"
    search_fields = [
        "$onsetDateTime",
        "$onsetString",
    ]


class AllergyIntolerance_Reaction(viewsets.ModelViewSet):
    queryset = models.AllergyIntolerance_Reaction.objects.all()
    serializer_class = serializers.AllergyIntolerance_Reaction
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.AllergyIntolerance_Reaction
    ordering_fields = "__all__"


class Appointment(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.Appointment
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Appointment
    ordering_fields = "__all__"


class Appointment_Participant(viewsets.ModelViewSet):
    queryset = models.Appointment_Participant.objects.all()
    serializer_class = serializers.Appointment_Participant
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Appointment_Participant
    ordering_fields = "__all__"


class AppointmentResponse(viewsets.ModelViewSet):
    queryset = models.AppointmentResponse.objects.all()
    serializer_class = serializers.AppointmentResponse
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.AppointmentResponse
    ordering_fields = "__all__"


class AuditEvent(viewsets.ModelViewSet):
    queryset = models.AuditEvent.objects.all()
    serializer_class = serializers.AuditEvent
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.AuditEvent
    ordering_fields = "__all__"


class AuditEvent_Agent(viewsets.ModelViewSet):
    queryset = models.AuditEvent_Agent.objects.all()
    serializer_class = serializers.AuditEvent_Agent
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.AuditEvent_Agent
    ordering_fields = "__all__"


class AuditEvent_Network(viewsets.ModelViewSet):
    queryset = models.AuditEvent_Network.objects.all()
    serializer_class = serializers.AuditEvent_Network
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.AuditEvent_Network
    ordering_fields = "__all__"


class AuditEvent_Source(viewsets.ModelViewSet):
    queryset = models.AuditEvent_Source.objects.all()
    serializer_class = serializers.AuditEvent_Source
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.AuditEvent_Source
    ordering_fields = "__all__"


class AuditEvent_Entity(viewsets.ModelViewSet):
    queryset = models.AuditEvent_Entity.objects.all()
    serializer_class = serializers.AuditEvent_Entity
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.AuditEvent_Entity
    ordering_fields = "__all__"


class AuditEvent_Detail(viewsets.ModelViewSet):
    queryset = models.AuditEvent_Detail.objects.all()
    serializer_class = serializers.AuditEvent_Detail
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.AuditEvent_Detail
    ordering_fields = "__all__"
    search_fields = [
        "$valueString",
        "$valueBase64Binary",
    ]


class Basic(viewsets.ModelViewSet):
    queryset = models.Basic.objects.all()
    serializer_class = serializers.Basic
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Basic
    ordering_fields = "__all__"


class Binary(viewsets.ModelViewSet):
    queryset = models.Binary.objects.all()
    serializer_class = serializers.Binary
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Binary
    ordering_fields = "__all__"


class BiologicallyDerivedProduct(viewsets.ModelViewSet):
    queryset = models.BiologicallyDerivedProduct.objects.all()
    serializer_class = serializers.BiologicallyDerivedProduct
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.BiologicallyDerivedProduct
    ordering_fields = "__all__"


class BiologicallyDerivedProduct_Collection(viewsets.ModelViewSet):
    queryset = models.BiologicallyDerivedProduct_Collection.objects.all()
    serializer_class = serializers.BiologicallyDerivedProduct_Collection
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.BiologicallyDerivedProduct_Collection
    ordering_fields = "__all__"
    search_fields = [
        "$collectedDateTime",
    ]


class BiologicallyDerivedProduct_Processing(viewsets.ModelViewSet):
    queryset = models.BiologicallyDerivedProduct_Processing.objects.all()
    serializer_class = serializers.BiologicallyDerivedProduct_Processing
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.BiologicallyDerivedProduct_Processing
    ordering_fields = "__all__"
    search_fields = [
        "$timeDateTime",
    ]


class BiologicallyDerivedProduct_Manipulation(viewsets.ModelViewSet):
    queryset = models.BiologicallyDerivedProduct_Manipulation.objects.all()
    serializer_class = serializers.BiologicallyDerivedProduct_Manipulation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.BiologicallyDerivedProduct_Manipulation
    ordering_fields = "__all__"
    search_fields = [
        "$timeDateTime",
    ]


class BiologicallyDerivedProduct_Storage(viewsets.ModelViewSet):
    queryset = models.BiologicallyDerivedProduct_Storage.objects.all()
    serializer_class = serializers.BiologicallyDerivedProduct_Storage
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.BiologicallyDerivedProduct_Storage
    ordering_fields = "__all__"


class BodyStructure(viewsets.ModelViewSet):
    queryset = models.BodyStructure.objects.all()
    serializer_class = serializers.BodyStructure
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.BodyStructure
    ordering_fields = "__all__"


class Bundle(viewsets.ModelViewSet):
    queryset = models.Bundle.objects.all()
    serializer_class = serializers.Bundle
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Bundle
    ordering_fields = "__all__"


class Bundle_Link(viewsets.ModelViewSet):
    queryset = models.Bundle_Link.objects.all()
    serializer_class = serializers.Bundle_Link
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Bundle_Link
    ordering_fields = "__all__"


class Bundle_Entry(viewsets.ModelViewSet):
    queryset = models.Bundle_Entry.objects.all()
    serializer_class = serializers.Bundle_Entry
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Bundle_Entry
    ordering_fields = "__all__"


class Bundle_Search(viewsets.ModelViewSet):
    queryset = models.Bundle_Search.objects.all()
    serializer_class = serializers.Bundle_Search
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Bundle_Search
    ordering_fields = "__all__"


class Bundle_Request(viewsets.ModelViewSet):
    queryset = models.Bundle_Request.objects.all()
    serializer_class = serializers.Bundle_Request
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Bundle_Request
    ordering_fields = "__all__"


class Bundle_Response(viewsets.ModelViewSet):
    queryset = models.Bundle_Response.objects.all()
    serializer_class = serializers.Bundle_Response
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Bundle_Response
    ordering_fields = "__all__"


class CapabilityStatement(viewsets.ModelViewSet):
    queryset = models.CapabilityStatement.objects.all()
    serializer_class = serializers.CapabilityStatement
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CapabilityStatement
    ordering_fields = "__all__"


class CapabilityStatement_Software(viewsets.ModelViewSet):
    queryset = models.CapabilityStatement_Software.objects.all()
    serializer_class = serializers.CapabilityStatement_Software
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CapabilityStatement_Software
    ordering_fields = "__all__"


class CapabilityStatement_Implementation(viewsets.ModelViewSet):
    queryset = models.CapabilityStatement_Implementation.objects.all()
    serializer_class = serializers.CapabilityStatement_Implementation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CapabilityStatement_Implementation
    ordering_fields = "__all__"


class CapabilityStatement_Rest(viewsets.ModelViewSet):
    queryset = models.CapabilityStatement_Rest.objects.all()
    serializer_class = serializers.CapabilityStatement_Rest
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CapabilityStatement_Rest
    ordering_fields = "__all__"


class CapabilityStatement_Security(viewsets.ModelViewSet):
    queryset = models.CapabilityStatement_Security.objects.all()
    serializer_class = serializers.CapabilityStatement_Security
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CapabilityStatement_Security
    ordering_fields = "__all__"


class CapabilityStatement_Resource(viewsets.ModelViewSet):
    queryset = models.CapabilityStatement_Resource.objects.all()
    serializer_class = serializers.CapabilityStatement_Resource
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CapabilityStatement_Resource
    ordering_fields = "__all__"


class CapabilityStatement_Interaction(viewsets.ModelViewSet):
    queryset = models.CapabilityStatement_Interaction.objects.all()
    serializer_class = serializers.CapabilityStatement_Interaction
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CapabilityStatement_Interaction
    ordering_fields = "__all__"


class CapabilityStatement_SearchParam(viewsets.ModelViewSet):
    queryset = models.CapabilityStatement_SearchParam.objects.all()
    serializer_class = serializers.CapabilityStatement_SearchParam
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CapabilityStatement_SearchParam
    ordering_fields = "__all__"


class CapabilityStatement_Operation(viewsets.ModelViewSet):
    queryset = models.CapabilityStatement_Operation.objects.all()
    serializer_class = serializers.CapabilityStatement_Operation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CapabilityStatement_Operation
    ordering_fields = "__all__"


class CapabilityStatement_Interaction1(viewsets.ModelViewSet):
    queryset = models.CapabilityStatement_Interaction1.objects.all()
    serializer_class = serializers.CapabilityStatement_Interaction1
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CapabilityStatement_Interaction1
    ordering_fields = "__all__"


class CapabilityStatement_Messaging(viewsets.ModelViewSet):
    queryset = models.CapabilityStatement_Messaging.objects.all()
    serializer_class = serializers.CapabilityStatement_Messaging
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CapabilityStatement_Messaging
    ordering_fields = "__all__"


class CapabilityStatement_Endpoint(viewsets.ModelViewSet):
    queryset = models.CapabilityStatement_Endpoint.objects.all()
    serializer_class = serializers.CapabilityStatement_Endpoint
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CapabilityStatement_Endpoint
    ordering_fields = "__all__"


class CapabilityStatement_SupportedMessage(viewsets.ModelViewSet):
    queryset = models.CapabilityStatement_SupportedMessage.objects.all()
    serializer_class = serializers.CapabilityStatement_SupportedMessage
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CapabilityStatement_SupportedMessage
    ordering_fields = "__all__"


class CapabilityStatement_Document(viewsets.ModelViewSet):
    queryset = models.CapabilityStatement_Document.objects.all()
    serializer_class = serializers.CapabilityStatement_Document
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CapabilityStatement_Document
    ordering_fields = "__all__"


class CarePlan(viewsets.ModelViewSet):
    queryset = models.CarePlan.objects.all()
    serializer_class = serializers.CarePlan
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CarePlan
    ordering_fields = "__all__"


class CarePlan_Activity(viewsets.ModelViewSet):
    queryset = models.CarePlan_Activity.objects.all()
    serializer_class = serializers.CarePlan_Activity
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CarePlan_Activity
    ordering_fields = "__all__"


class CarePlan_Detail(viewsets.ModelViewSet):
    queryset = models.CarePlan_Detail.objects.all()
    serializer_class = serializers.CarePlan_Detail
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CarePlan_Detail
    ordering_fields = "__all__"
    search_fields = [
        "$scheduledString",
    ]


class CareTeam(viewsets.ModelViewSet):
    queryset = models.CareTeam.objects.all()
    serializer_class = serializers.CareTeam
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CareTeam
    ordering_fields = "__all__"


class CareTeam_Participant(viewsets.ModelViewSet):
    queryset = models.CareTeam_Participant.objects.all()
    serializer_class = serializers.CareTeam_Participant
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CareTeam_Participant
    ordering_fields = "__all__"


class CatalogEntry(viewsets.ModelViewSet):
    queryset = models.CatalogEntry.objects.all()
    serializer_class = serializers.CatalogEntry
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CatalogEntry
    ordering_fields = "__all__"


class CatalogEntry_RelatedEntry(viewsets.ModelViewSet):
    queryset = models.CatalogEntry_RelatedEntry.objects.all()
    serializer_class = serializers.CatalogEntry_RelatedEntry
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CatalogEntry_RelatedEntry
    ordering_fields = "__all__"


class ChargeItem(viewsets.ModelViewSet):
    queryset = models.ChargeItem.objects.all()
    serializer_class = serializers.ChargeItem
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ChargeItem
    ordering_fields = "__all__"
    search_fields = [
        "$occurrenceDateTime",
    ]


class ChargeItem_Performer(viewsets.ModelViewSet):
    queryset = models.ChargeItem_Performer.objects.all()
    serializer_class = serializers.ChargeItem_Performer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ChargeItem_Performer
    ordering_fields = "__all__"


class ChargeItemDefinition(viewsets.ModelViewSet):
    queryset = models.ChargeItemDefinition.objects.all()
    serializer_class = serializers.ChargeItemDefinition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ChargeItemDefinition
    ordering_fields = "__all__"


class ChargeItemDefinition_Applicability(viewsets.ModelViewSet):
    queryset = models.ChargeItemDefinition_Applicability.objects.all()
    serializer_class = serializers.ChargeItemDefinition_Applicability
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ChargeItemDefinition_Applicability
    ordering_fields = "__all__"


class ChargeItemDefinition_PropertyGroup(viewsets.ModelViewSet):
    queryset = models.ChargeItemDefinition_PropertyGroup.objects.all()
    serializer_class = serializers.ChargeItemDefinition_PropertyGroup
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ChargeItemDefinition_PropertyGroup
    ordering_fields = "__all__"


class ChargeItemDefinition_PriceComponent(viewsets.ModelViewSet):
    queryset = models.ChargeItemDefinition_PriceComponent.objects.all()
    serializer_class = serializers.ChargeItemDefinition_PriceComponent
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ChargeItemDefinition_PriceComponent
    ordering_fields = "__all__"


class Claim(viewsets.ModelViewSet):
    queryset = models.Claim.objects.all()
    serializer_class = serializers.Claim
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Claim
    ordering_fields = "__all__"


class Claim_Related(viewsets.ModelViewSet):
    queryset = models.Claim_Related.objects.all()
    serializer_class = serializers.Claim_Related
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Claim_Related
    ordering_fields = "__all__"


class Claim_Payee(viewsets.ModelViewSet):
    queryset = models.Claim_Payee.objects.all()
    serializer_class = serializers.Claim_Payee
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Claim_Payee
    ordering_fields = "__all__"


class Claim_CareTeam(viewsets.ModelViewSet):
    queryset = models.Claim_CareTeam.objects.all()
    serializer_class = serializers.Claim_CareTeam
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Claim_CareTeam
    ordering_fields = "__all__"


class Claim_SupportingInfo(viewsets.ModelViewSet):
    queryset = models.Claim_SupportingInfo.objects.all()
    serializer_class = serializers.Claim_SupportingInfo
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Claim_SupportingInfo
    ordering_fields = "__all__"
    search_fields = [
        "$timingDate",
        "$valueString",
    ]


class Claim_Diagnosis(viewsets.ModelViewSet):
    queryset = models.Claim_Diagnosis.objects.all()
    serializer_class = serializers.Claim_Diagnosis
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Claim_Diagnosis
    ordering_fields = "__all__"


class Claim_Procedure(viewsets.ModelViewSet):
    queryset = models.Claim_Procedure.objects.all()
    serializer_class = serializers.Claim_Procedure
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Claim_Procedure
    ordering_fields = "__all__"


class Claim_Insurance(viewsets.ModelViewSet):
    queryset = models.Claim_Insurance.objects.all()
    serializer_class = serializers.Claim_Insurance
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Claim_Insurance
    ordering_fields = "__all__"


class Claim_Accident(viewsets.ModelViewSet):
    queryset = models.Claim_Accident.objects.all()
    serializer_class = serializers.Claim_Accident
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Claim_Accident
    ordering_fields = "__all__"


class Claim_Item(viewsets.ModelViewSet):
    queryset = models.Claim_Item.objects.all()
    serializer_class = serializers.Claim_Item
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Claim_Item
    ordering_fields = "__all__"
    search_fields = [
        "$servicedDate",
    ]


class Claim_Detail(viewsets.ModelViewSet):
    queryset = models.Claim_Detail.objects.all()
    serializer_class = serializers.Claim_Detail
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Claim_Detail
    ordering_fields = "__all__"


class Claim_SubDetail(viewsets.ModelViewSet):
    queryset = models.Claim_SubDetail.objects.all()
    serializer_class = serializers.Claim_SubDetail
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Claim_SubDetail
    ordering_fields = "__all__"


class ClaimResponse(viewsets.ModelViewSet):
    queryset = models.ClaimResponse.objects.all()
    serializer_class = serializers.ClaimResponse
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ClaimResponse
    ordering_fields = "__all__"


class ClaimResponse_Item(viewsets.ModelViewSet):
    queryset = models.ClaimResponse_Item.objects.all()
    serializer_class = serializers.ClaimResponse_Item
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ClaimResponse_Item
    ordering_fields = "__all__"


class ClaimResponse_Adjudication(viewsets.ModelViewSet):
    queryset = models.ClaimResponse_Adjudication.objects.all()
    serializer_class = serializers.ClaimResponse_Adjudication
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ClaimResponse_Adjudication
    ordering_fields = "__all__"


class ClaimResponse_Detail(viewsets.ModelViewSet):
    queryset = models.ClaimResponse_Detail.objects.all()
    serializer_class = serializers.ClaimResponse_Detail
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ClaimResponse_Detail
    ordering_fields = "__all__"


class ClaimResponse_SubDetail(viewsets.ModelViewSet):
    queryset = models.ClaimResponse_SubDetail.objects.all()
    serializer_class = serializers.ClaimResponse_SubDetail
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ClaimResponse_SubDetail
    ordering_fields = "__all__"


class ClaimResponse_AddItem(viewsets.ModelViewSet):
    queryset = models.ClaimResponse_AddItem.objects.all()
    serializer_class = serializers.ClaimResponse_AddItem
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ClaimResponse_AddItem
    ordering_fields = "__all__"
    search_fields = [
        "$servicedDate",
    ]


class ClaimResponse_Detail1(viewsets.ModelViewSet):
    queryset = models.ClaimResponse_Detail1.objects.all()
    serializer_class = serializers.ClaimResponse_Detail1
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ClaimResponse_Detail1
    ordering_fields = "__all__"


class ClaimResponse_SubDetail1(viewsets.ModelViewSet):
    queryset = models.ClaimResponse_SubDetail1.objects.all()
    serializer_class = serializers.ClaimResponse_SubDetail1
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ClaimResponse_SubDetail1
    ordering_fields = "__all__"


class ClaimResponse_Total(viewsets.ModelViewSet):
    queryset = models.ClaimResponse_Total.objects.all()
    serializer_class = serializers.ClaimResponse_Total
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ClaimResponse_Total
    ordering_fields = "__all__"


class ClaimResponse_Payment(viewsets.ModelViewSet):
    queryset = models.ClaimResponse_Payment.objects.all()
    serializer_class = serializers.ClaimResponse_Payment
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ClaimResponse_Payment
    ordering_fields = "__all__"


class ClaimResponse_ProcessNote(viewsets.ModelViewSet):
    queryset = models.ClaimResponse_ProcessNote.objects.all()
    serializer_class = serializers.ClaimResponse_ProcessNote
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ClaimResponse_ProcessNote
    ordering_fields = "__all__"


class ClaimResponse_Insurance(viewsets.ModelViewSet):
    queryset = models.ClaimResponse_Insurance.objects.all()
    serializer_class = serializers.ClaimResponse_Insurance
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ClaimResponse_Insurance
    ordering_fields = "__all__"


class ClaimResponse_Error(viewsets.ModelViewSet):
    queryset = models.ClaimResponse_Error.objects.all()
    serializer_class = serializers.ClaimResponse_Error
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ClaimResponse_Error
    ordering_fields = "__all__"


class ClinicalImpression(viewsets.ModelViewSet):
    queryset = models.ClinicalImpression.objects.all()
    serializer_class = serializers.ClinicalImpression
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ClinicalImpression
    ordering_fields = "__all__"
    search_fields = [
        "$effectiveDateTime",
    ]


class ClinicalImpression_Investigation(viewsets.ModelViewSet):
    queryset = models.ClinicalImpression_Investigation.objects.all()
    serializer_class = serializers.ClinicalImpression_Investigation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ClinicalImpression_Investigation
    ordering_fields = "__all__"


class ClinicalImpression_Finding(viewsets.ModelViewSet):
    queryset = models.ClinicalImpression_Finding.objects.all()
    serializer_class = serializers.ClinicalImpression_Finding
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ClinicalImpression_Finding
    ordering_fields = "__all__"


class CodeSystem(viewsets.ModelViewSet):
    queryset = models.CodeSystem.objects.all()
    serializer_class = serializers.CodeSystem
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CodeSystem
    ordering_fields = "__all__"


class CodeSystem_Filter(viewsets.ModelViewSet):
    queryset = models.CodeSystem_Filter.objects.all()
    serializer_class = serializers.CodeSystem_Filter
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CodeSystem_Filter
    ordering_fields = "__all__"


class CodeSystem_Property(viewsets.ModelViewSet):
    queryset = models.CodeSystem_Property.objects.all()
    serializer_class = serializers.CodeSystem_Property
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CodeSystem_Property
    ordering_fields = "__all__"


class CodeSystem_Concept(viewsets.ModelViewSet):
    queryset = models.CodeSystem_Concept.objects.all()
    serializer_class = serializers.CodeSystem_Concept
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CodeSystem_Concept
    ordering_fields = "__all__"


class CodeSystem_Designation(viewsets.ModelViewSet):
    queryset = models.CodeSystem_Designation.objects.all()
    serializer_class = serializers.CodeSystem_Designation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CodeSystem_Designation
    ordering_fields = "__all__"


class CodeSystem_Property1(viewsets.ModelViewSet):
    queryset = models.CodeSystem_Property1.objects.all()
    serializer_class = serializers.CodeSystem_Property1
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CodeSystem_Property1
    ordering_fields = "__all__"
    search_fields = [
        "$valueCode",
        "$valueString",
        "$valueDateTime",
    ]


class Communication(viewsets.ModelViewSet):
    queryset = models.Communication.objects.all()
    serializer_class = serializers.Communication
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Communication
    ordering_fields = "__all__"


class Communication_Payload(viewsets.ModelViewSet):
    queryset = models.Communication_Payload.objects.all()
    serializer_class = serializers.Communication_Payload
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Communication_Payload
    ordering_fields = "__all__"
    search_fields = [
        "$contentString",
    ]


class CommunicationRequest(viewsets.ModelViewSet):
    queryset = models.CommunicationRequest.objects.all()
    serializer_class = serializers.CommunicationRequest
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CommunicationRequest
    ordering_fields = "__all__"
    search_fields = [
        "$occurrenceDateTime",
    ]


class CommunicationRequest_Payload(viewsets.ModelViewSet):
    queryset = models.CommunicationRequest_Payload.objects.all()
    serializer_class = serializers.CommunicationRequest_Payload
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CommunicationRequest_Payload
    ordering_fields = "__all__"
    search_fields = [
        "$contentString",
    ]


class CompartmentDefinition(viewsets.ModelViewSet):
    queryset = models.CompartmentDefinition.objects.all()
    serializer_class = serializers.CompartmentDefinition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CompartmentDefinition
    ordering_fields = "__all__"


class CompartmentDefinition_Resource(viewsets.ModelViewSet):
    queryset = models.CompartmentDefinition_Resource.objects.all()
    serializer_class = serializers.CompartmentDefinition_Resource
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CompartmentDefinition_Resource
    ordering_fields = "__all__"


class Composition(viewsets.ModelViewSet):
    queryset = models.Composition.objects.all()
    serializer_class = serializers.Composition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Composition
    ordering_fields = "__all__"


class Composition_Attester(viewsets.ModelViewSet):
    queryset = models.Composition_Attester.objects.all()
    serializer_class = serializers.Composition_Attester
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Composition_Attester
    ordering_fields = "__all__"


class Composition_RelatesTo(viewsets.ModelViewSet):
    queryset = models.Composition_RelatesTo.objects.all()
    serializer_class = serializers.Composition_RelatesTo
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Composition_RelatesTo
    ordering_fields = "__all__"


class Composition_Event(viewsets.ModelViewSet):
    queryset = models.Composition_Event.objects.all()
    serializer_class = serializers.Composition_Event
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Composition_Event
    ordering_fields = "__all__"


class Composition_Section(viewsets.ModelViewSet):
    queryset = models.Composition_Section.objects.all()
    serializer_class = serializers.Composition_Section
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Composition_Section
    ordering_fields = "__all__"


class ConceptMap(viewsets.ModelViewSet):
    queryset = models.ConceptMap.objects.all()
    serializer_class = serializers.ConceptMap
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ConceptMap
    ordering_fields = "__all__"
    search_fields = [
        "$sourceUri",
        "$sourceCanonical",
        "$targetUri",
        "$targetCanonical",
    ]


class ConceptMap_Group(viewsets.ModelViewSet):
    queryset = models.ConceptMap_Group.objects.all()
    serializer_class = serializers.ConceptMap_Group
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ConceptMap_Group
    ordering_fields = "__all__"


class ConceptMap_Element(viewsets.ModelViewSet):
    queryset = models.ConceptMap_Element.objects.all()
    serializer_class = serializers.ConceptMap_Element
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ConceptMap_Element
    ordering_fields = "__all__"


class ConceptMap_Target(viewsets.ModelViewSet):
    queryset = models.ConceptMap_Target.objects.all()
    serializer_class = serializers.ConceptMap_Target
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ConceptMap_Target
    ordering_fields = "__all__"


class ConceptMap_DependsOn(viewsets.ModelViewSet):
    queryset = models.ConceptMap_DependsOn.objects.all()
    serializer_class = serializers.ConceptMap_DependsOn
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ConceptMap_DependsOn
    ordering_fields = "__all__"


class ConceptMap_Unmapped(viewsets.ModelViewSet):
    queryset = models.ConceptMap_Unmapped.objects.all()
    serializer_class = serializers.ConceptMap_Unmapped
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ConceptMap_Unmapped
    ordering_fields = "__all__"


class Condition(viewsets.ModelViewSet):
    queryset = models.Condition.objects.all()
    serializer_class = serializers.Condition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Condition
    ordering_fields = "__all__"
    search_fields = [
        "$onsetDateTime",
        "$onsetString",
        "$abatementDateTime",
        "$abatementString",
    ]


class Condition_Stage(viewsets.ModelViewSet):
    queryset = models.Condition_Stage.objects.all()
    serializer_class = serializers.Condition_Stage
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Condition_Stage
    ordering_fields = "__all__"


class Condition_Evidence(viewsets.ModelViewSet):
    queryset = models.Condition_Evidence.objects.all()
    serializer_class = serializers.Condition_Evidence
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Condition_Evidence
    ordering_fields = "__all__"


class Consent(viewsets.ModelViewSet):
    queryset = models.Consent.objects.all()
    serializer_class = serializers.Consent
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Consent
    ordering_fields = "__all__"


class Consent_Policy(viewsets.ModelViewSet):
    queryset = models.Consent_Policy.objects.all()
    serializer_class = serializers.Consent_Policy
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Consent_Policy
    ordering_fields = "__all__"


class Consent_Verification(viewsets.ModelViewSet):
    queryset = models.Consent_Verification.objects.all()
    serializer_class = serializers.Consent_Verification
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Consent_Verification
    ordering_fields = "__all__"


class Consent_Provision(viewsets.ModelViewSet):
    queryset = models.Consent_Provision.objects.all()
    serializer_class = serializers.Consent_Provision
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Consent_Provision
    ordering_fields = "__all__"


class Consent_Actor(viewsets.ModelViewSet):
    queryset = models.Consent_Actor.objects.all()
    serializer_class = serializers.Consent_Actor
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Consent_Actor
    ordering_fields = "__all__"


class Consent_Data(viewsets.ModelViewSet):
    queryset = models.Consent_Data.objects.all()
    serializer_class = serializers.Consent_Data
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Consent_Data
    ordering_fields = "__all__"


class Contract(viewsets.ModelViewSet):
    queryset = models.Contract.objects.all()
    serializer_class = serializers.Contract
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Contract
    ordering_fields = "__all__"


class Contract_ContentDefinition(viewsets.ModelViewSet):
    queryset = models.Contract_ContentDefinition.objects.all()
    serializer_class = serializers.Contract_ContentDefinition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Contract_ContentDefinition
    ordering_fields = "__all__"


class Contract_Term(viewsets.ModelViewSet):
    queryset = models.Contract_Term.objects.all()
    serializer_class = serializers.Contract_Term
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Contract_Term
    ordering_fields = "__all__"


class Contract_SecurityLabel(viewsets.ModelViewSet):
    queryset = models.Contract_SecurityLabel.objects.all()
    serializer_class = serializers.Contract_SecurityLabel
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Contract_SecurityLabel
    ordering_fields = "__all__"


class Contract_Offer(viewsets.ModelViewSet):
    queryset = models.Contract_Offer.objects.all()
    serializer_class = serializers.Contract_Offer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Contract_Offer
    ordering_fields = "__all__"


class Contract_Party(viewsets.ModelViewSet):
    queryset = models.Contract_Party.objects.all()
    serializer_class = serializers.Contract_Party
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Contract_Party
    ordering_fields = "__all__"


class Contract_Answer(viewsets.ModelViewSet):
    queryset = models.Contract_Answer.objects.all()
    serializer_class = serializers.Contract_Answer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Contract_Answer
    ordering_fields = "__all__"
    search_fields = [
        "$valueDate",
        "$valueDateTime",
        "$valueTime",
        "$valueString",
        "$valueUri",
    ]


class Contract_Asset(viewsets.ModelViewSet):
    queryset = models.Contract_Asset.objects.all()
    serializer_class = serializers.Contract_Asset
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Contract_Asset
    ordering_fields = "__all__"


class Contract_Context(viewsets.ModelViewSet):
    queryset = models.Contract_Context.objects.all()
    serializer_class = serializers.Contract_Context
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Contract_Context
    ordering_fields = "__all__"


class Contract_ValuedItem(viewsets.ModelViewSet):
    queryset = models.Contract_ValuedItem.objects.all()
    serializer_class = serializers.Contract_ValuedItem
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Contract_ValuedItem
    ordering_fields = "__all__"


class Contract_Action(viewsets.ModelViewSet):
    queryset = models.Contract_Action.objects.all()
    serializer_class = serializers.Contract_Action
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Contract_Action
    ordering_fields = "__all__"
    search_fields = [
        "$occurrenceDateTime",
    ]


class Contract_Subject(viewsets.ModelViewSet):
    queryset = models.Contract_Subject.objects.all()
    serializer_class = serializers.Contract_Subject
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Contract_Subject
    ordering_fields = "__all__"


class Contract_Signer(viewsets.ModelViewSet):
    queryset = models.Contract_Signer.objects.all()
    serializer_class = serializers.Contract_Signer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Contract_Signer
    ordering_fields = "__all__"


class Contract_Friendly(viewsets.ModelViewSet):
    queryset = models.Contract_Friendly.objects.all()
    serializer_class = serializers.Contract_Friendly
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Contract_Friendly
    ordering_fields = "__all__"


class Contract_Legal(viewsets.ModelViewSet):
    queryset = models.Contract_Legal.objects.all()
    serializer_class = serializers.Contract_Legal
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Contract_Legal
    ordering_fields = "__all__"


class Contract_Rule(viewsets.ModelViewSet):
    queryset = models.Contract_Rule.objects.all()
    serializer_class = serializers.Contract_Rule
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Contract_Rule
    ordering_fields = "__all__"


class Coverage(viewsets.ModelViewSet):
    queryset = models.Coverage.objects.all()
    serializer_class = serializers.Coverage
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Coverage
    ordering_fields = "__all__"


class Coverage_Class(viewsets.ModelViewSet):
    queryset = models.Coverage_Class.objects.all()
    serializer_class = serializers.Coverage_Class
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Coverage_Class
    ordering_fields = "__all__"


class Coverage_CostToBeneficiary(viewsets.ModelViewSet):
    queryset = models.Coverage_CostToBeneficiary.objects.all()
    serializer_class = serializers.Coverage_CostToBeneficiary
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Coverage_CostToBeneficiary
    ordering_fields = "__all__"


class Coverage_Exception(viewsets.ModelViewSet):
    queryset = models.Coverage_Exception.objects.all()
    serializer_class = serializers.Coverage_Exception
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Coverage_Exception
    ordering_fields = "__all__"


class CoverageEligibilityRequest(viewsets.ModelViewSet):
    queryset = models.CoverageEligibilityRequest.objects.all()
    serializer_class = serializers.CoverageEligibilityRequest
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CoverageEligibilityRequest
    ordering_fields = "__all__"
    search_fields = [
        "$servicedDate",
    ]


class CoverageEligibilityRequest_SupportingInfo(viewsets.ModelViewSet):
    queryset = models.CoverageEligibilityRequest_SupportingInfo.objects.all()
    serializer_class = serializers.CoverageEligibilityRequest_SupportingInfo
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CoverageEligibilityRequest_SupportingInfo
    ordering_fields = "__all__"


class CoverageEligibilityRequest_Insurance(viewsets.ModelViewSet):
    queryset = models.CoverageEligibilityRequest_Insurance.objects.all()
    serializer_class = serializers.CoverageEligibilityRequest_Insurance
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CoverageEligibilityRequest_Insurance
    ordering_fields = "__all__"


class CoverageEligibilityRequest_Item(viewsets.ModelViewSet):
    queryset = models.CoverageEligibilityRequest_Item.objects.all()
    serializer_class = serializers.CoverageEligibilityRequest_Item
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CoverageEligibilityRequest_Item
    ordering_fields = "__all__"


class CoverageEligibilityRequest_Diagnosis(viewsets.ModelViewSet):
    queryset = models.CoverageEligibilityRequest_Diagnosis.objects.all()
    serializer_class = serializers.CoverageEligibilityRequest_Diagnosis
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CoverageEligibilityRequest_Diagnosis
    ordering_fields = "__all__"


class CoverageEligibilityResponse(viewsets.ModelViewSet):
    queryset = models.CoverageEligibilityResponse.objects.all()
    serializer_class = serializers.CoverageEligibilityResponse
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CoverageEligibilityResponse
    ordering_fields = "__all__"
    search_fields = [
        "$servicedDate",
    ]


class CoverageEligibilityResponse_Insurance(viewsets.ModelViewSet):
    queryset = models.CoverageEligibilityResponse_Insurance.objects.all()
    serializer_class = serializers.CoverageEligibilityResponse_Insurance
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CoverageEligibilityResponse_Insurance
    ordering_fields = "__all__"


class CoverageEligibilityResponse_Item(viewsets.ModelViewSet):
    queryset = models.CoverageEligibilityResponse_Item.objects.all()
    serializer_class = serializers.CoverageEligibilityResponse_Item
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CoverageEligibilityResponse_Item
    ordering_fields = "__all__"


class CoverageEligibilityResponse_Benefit(viewsets.ModelViewSet):
    queryset = models.CoverageEligibilityResponse_Benefit.objects.all()
    serializer_class = serializers.CoverageEligibilityResponse_Benefit
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CoverageEligibilityResponse_Benefit
    ordering_fields = "__all__"
    search_fields = [
        "$allowedString",
        "$usedString",
    ]


class CoverageEligibilityResponse_Error(viewsets.ModelViewSet):
    queryset = models.CoverageEligibilityResponse_Error.objects.all()
    serializer_class = serializers.CoverageEligibilityResponse_Error
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CoverageEligibilityResponse_Error
    ordering_fields = "__all__"


class DetectedIssue(viewsets.ModelViewSet):
    queryset = models.DetectedIssue.objects.all()
    serializer_class = serializers.DetectedIssue
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DetectedIssue
    ordering_fields = "__all__"
    search_fields = [
        "$identifiedDateTime",
    ]


class DetectedIssue_Evidence(viewsets.ModelViewSet):
    queryset = models.DetectedIssue_Evidence.objects.all()
    serializer_class = serializers.DetectedIssue_Evidence
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DetectedIssue_Evidence
    ordering_fields = "__all__"


class DetectedIssue_Mitigation(viewsets.ModelViewSet):
    queryset = models.DetectedIssue_Mitigation.objects.all()
    serializer_class = serializers.DetectedIssue_Mitigation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DetectedIssue_Mitigation
    ordering_fields = "__all__"


class Device(viewsets.ModelViewSet):
    queryset = models.Device.objects.all()
    serializer_class = serializers.Device
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Device
    ordering_fields = "__all__"


class Device_UdiCarrier(viewsets.ModelViewSet):
    queryset = models.Device_UdiCarrier.objects.all()
    serializer_class = serializers.Device_UdiCarrier
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Device_UdiCarrier
    ordering_fields = "__all__"


class Device_DeviceName(viewsets.ModelViewSet):
    queryset = models.Device_DeviceName.objects.all()
    serializer_class = serializers.Device_DeviceName
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Device_DeviceName
    ordering_fields = "__all__"


class Device_Specialization(viewsets.ModelViewSet):
    queryset = models.Device_Specialization.objects.all()
    serializer_class = serializers.Device_Specialization
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Device_Specialization
    ordering_fields = "__all__"


class Device_Version(viewsets.ModelViewSet):
    queryset = models.Device_Version.objects.all()
    serializer_class = serializers.Device_Version
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Device_Version
    ordering_fields = "__all__"


class Device_Property(viewsets.ModelViewSet):
    queryset = models.Device_Property.objects.all()
    serializer_class = serializers.Device_Property
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Device_Property
    ordering_fields = "__all__"


class DeviceDefinition(viewsets.ModelViewSet):
    queryset = models.DeviceDefinition.objects.all()
    serializer_class = serializers.DeviceDefinition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DeviceDefinition
    ordering_fields = "__all__"
    search_fields = [
        "$manufacturerString",
    ]


class DeviceDefinition_UdiDeviceIdentifier(viewsets.ModelViewSet):
    queryset = models.DeviceDefinition_UdiDeviceIdentifier.objects.all()
    serializer_class = serializers.DeviceDefinition_UdiDeviceIdentifier
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DeviceDefinition_UdiDeviceIdentifier
    ordering_fields = "__all__"


class DeviceDefinition_DeviceName(viewsets.ModelViewSet):
    queryset = models.DeviceDefinition_DeviceName.objects.all()
    serializer_class = serializers.DeviceDefinition_DeviceName
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DeviceDefinition_DeviceName
    ordering_fields = "__all__"


class DeviceDefinition_Specialization(viewsets.ModelViewSet):
    queryset = models.DeviceDefinition_Specialization.objects.all()
    serializer_class = serializers.DeviceDefinition_Specialization
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DeviceDefinition_Specialization
    ordering_fields = "__all__"


class DeviceDefinition_Capability(viewsets.ModelViewSet):
    queryset = models.DeviceDefinition_Capability.objects.all()
    serializer_class = serializers.DeviceDefinition_Capability
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DeviceDefinition_Capability
    ordering_fields = "__all__"


class DeviceDefinition_Property(viewsets.ModelViewSet):
    queryset = models.DeviceDefinition_Property.objects.all()
    serializer_class = serializers.DeviceDefinition_Property
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DeviceDefinition_Property
    ordering_fields = "__all__"


class DeviceDefinition_Material(viewsets.ModelViewSet):
    queryset = models.DeviceDefinition_Material.objects.all()
    serializer_class = serializers.DeviceDefinition_Material
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DeviceDefinition_Material
    ordering_fields = "__all__"


class DeviceMetric(viewsets.ModelViewSet):
    queryset = models.DeviceMetric.objects.all()
    serializer_class = serializers.DeviceMetric
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DeviceMetric
    ordering_fields = "__all__"


class DeviceMetric_Calibration(viewsets.ModelViewSet):
    queryset = models.DeviceMetric_Calibration.objects.all()
    serializer_class = serializers.DeviceMetric_Calibration
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DeviceMetric_Calibration
    ordering_fields = "__all__"


class DeviceRequest(viewsets.ModelViewSet):
    queryset = models.DeviceRequest.objects.all()
    serializer_class = serializers.DeviceRequest
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DeviceRequest
    ordering_fields = "__all__"
    search_fields = [
        "$occurrenceDateTime",
    ]


class DeviceRequest_Parameter(viewsets.ModelViewSet):
    queryset = models.DeviceRequest_Parameter.objects.all()
    serializer_class = serializers.DeviceRequest_Parameter
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DeviceRequest_Parameter
    ordering_fields = "__all__"


class DeviceUseStatement(viewsets.ModelViewSet):
    queryset = models.DeviceUseStatement.objects.all()
    serializer_class = serializers.DeviceUseStatement
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DeviceUseStatement
    ordering_fields = "__all__"
    search_fields = [
        "$timingDateTime",
    ]


class DiagnosticReport(viewsets.ModelViewSet):
    queryset = models.DiagnosticReport.objects.all()
    serializer_class = serializers.DiagnosticReport
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DiagnosticReport
    ordering_fields = "__all__"
    search_fields = [
        "$effectiveDateTime",
    ]


class DiagnosticReport_Media(viewsets.ModelViewSet):
    queryset = models.DiagnosticReport_Media.objects.all()
    serializer_class = serializers.DiagnosticReport_Media
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DiagnosticReport_Media
    ordering_fields = "__all__"


class DocumentManifest(viewsets.ModelViewSet):
    queryset = models.DocumentManifest.objects.all()
    serializer_class = serializers.DocumentManifest
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DocumentManifest
    ordering_fields = "__all__"


class DocumentManifest_Related(viewsets.ModelViewSet):
    queryset = models.DocumentManifest_Related.objects.all()
    serializer_class = serializers.DocumentManifest_Related
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DocumentManifest_Related
    ordering_fields = "__all__"


class DocumentReference(viewsets.ModelViewSet):
    queryset = models.DocumentReference.objects.all()
    serializer_class = serializers.DocumentReference
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DocumentReference
    ordering_fields = "__all__"


class DocumentReference_RelatesTo(viewsets.ModelViewSet):
    queryset = models.DocumentReference_RelatesTo.objects.all()
    serializer_class = serializers.DocumentReference_RelatesTo
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DocumentReference_RelatesTo
    ordering_fields = "__all__"


class DocumentReference_Content(viewsets.ModelViewSet):
    queryset = models.DocumentReference_Content.objects.all()
    serializer_class = serializers.DocumentReference_Content
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DocumentReference_Content
    ordering_fields = "__all__"


class DocumentReference_Context(viewsets.ModelViewSet):
    queryset = models.DocumentReference_Context.objects.all()
    serializer_class = serializers.DocumentReference_Context
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.DocumentReference_Context
    ordering_fields = "__all__"


class EffectEvidenceSynthesis(viewsets.ModelViewSet):
    queryset = models.EffectEvidenceSynthesis.objects.all()
    serializer_class = serializers.EffectEvidenceSynthesis
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.EffectEvidenceSynthesis
    ordering_fields = "__all__"


class EffectEvidenceSynthesis_SampleSize(viewsets.ModelViewSet):
    queryset = models.EffectEvidenceSynthesis_SampleSize.objects.all()
    serializer_class = serializers.EffectEvidenceSynthesis_SampleSize
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.EffectEvidenceSynthesis_SampleSize
    ordering_fields = "__all__"


class EffectEvidenceSynthesis_ResultsByExposure(viewsets.ModelViewSet):
    queryset = models.EffectEvidenceSynthesis_ResultsByExposure.objects.all()
    serializer_class = serializers.EffectEvidenceSynthesis_ResultsByExposure
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.EffectEvidenceSynthesis_ResultsByExposure
    ordering_fields = "__all__"


class EffectEvidenceSynthesis_EffectEstimate(viewsets.ModelViewSet):
    queryset = models.EffectEvidenceSynthesis_EffectEstimate.objects.all()
    serializer_class = serializers.EffectEvidenceSynthesis_EffectEstimate
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.EffectEvidenceSynthesis_EffectEstimate
    ordering_fields = "__all__"


class EffectEvidenceSynthesis_PrecisionEstimate(viewsets.ModelViewSet):
    queryset = models.EffectEvidenceSynthesis_PrecisionEstimate.objects.all()
    serializer_class = serializers.EffectEvidenceSynthesis_PrecisionEstimate
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.EffectEvidenceSynthesis_PrecisionEstimate
    ordering_fields = "__all__"


class EffectEvidenceSynthesis_Certainty(viewsets.ModelViewSet):
    queryset = models.EffectEvidenceSynthesis_Certainty.objects.all()
    serializer_class = serializers.EffectEvidenceSynthesis_Certainty
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.EffectEvidenceSynthesis_Certainty
    ordering_fields = "__all__"


class EffectEvidenceSynthesis_CertaintySubcomponent(viewsets.ModelViewSet):
    queryset = models.EffectEvidenceSynthesis_CertaintySubcomponent.objects.all()
    serializer_class = serializers.EffectEvidenceSynthesis_CertaintySubcomponent
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.EffectEvidenceSynthesis_CertaintySubcomponent
    ordering_fields = "__all__"


class Encounter(viewsets.ModelViewSet):
    queryset = models.Encounter.objects.all()
    serializer_class = serializers.Encounter
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Encounter
    ordering_fields = "__all__"


class Encounter_StatusHistory(viewsets.ModelViewSet):
    queryset = models.Encounter_StatusHistory.objects.all()
    serializer_class = serializers.Encounter_StatusHistory
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Encounter_StatusHistory
    ordering_fields = "__all__"


class Encounter_ClassHistory(viewsets.ModelViewSet):
    queryset = models.Encounter_ClassHistory.objects.all()
    serializer_class = serializers.Encounter_ClassHistory
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Encounter_ClassHistory
    ordering_fields = "__all__"


class Encounter_Participant(viewsets.ModelViewSet):
    queryset = models.Encounter_Participant.objects.all()
    serializer_class = serializers.Encounter_Participant
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Encounter_Participant
    ordering_fields = "__all__"


class Encounter_Diagnosis(viewsets.ModelViewSet):
    queryset = models.Encounter_Diagnosis.objects.all()
    serializer_class = serializers.Encounter_Diagnosis
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Encounter_Diagnosis
    ordering_fields = "__all__"


class Encounter_Hospitalization(viewsets.ModelViewSet):
    queryset = models.Encounter_Hospitalization.objects.all()
    serializer_class = serializers.Encounter_Hospitalization
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Encounter_Hospitalization
    ordering_fields = "__all__"


class Encounter_Location(viewsets.ModelViewSet):
    queryset = models.Encounter_Location.objects.all()
    serializer_class = serializers.Encounter_Location
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Encounter_Location
    ordering_fields = "__all__"


class Endpoint(viewsets.ModelViewSet):
    queryset = models.Endpoint.objects.all()
    serializer_class = serializers.Endpoint
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Endpoint
    ordering_fields = "__all__"


class EnrollmentRequest(viewsets.ModelViewSet):
    queryset = models.EnrollmentRequest.objects.all()
    serializer_class = serializers.EnrollmentRequest
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.EnrollmentRequest
    ordering_fields = "__all__"


class EnrollmentResponse(viewsets.ModelViewSet):
    queryset = models.EnrollmentResponse.objects.all()
    serializer_class = serializers.EnrollmentResponse
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.EnrollmentResponse
    ordering_fields = "__all__"


class EpisodeOfCare(viewsets.ModelViewSet):
    queryset = models.EpisodeOfCare.objects.all()
    serializer_class = serializers.EpisodeOfCare
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.EpisodeOfCare
    ordering_fields = "__all__"


class EpisodeOfCare_StatusHistory(viewsets.ModelViewSet):
    queryset = models.EpisodeOfCare_StatusHistory.objects.all()
    serializer_class = serializers.EpisodeOfCare_StatusHistory
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.EpisodeOfCare_StatusHistory
    ordering_fields = "__all__"


class EpisodeOfCare_Diagnosis(viewsets.ModelViewSet):
    queryset = models.EpisodeOfCare_Diagnosis.objects.all()
    serializer_class = serializers.EpisodeOfCare_Diagnosis
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.EpisodeOfCare_Diagnosis
    ordering_fields = "__all__"


class EventDefinition(viewsets.ModelViewSet):
    queryset = models.EventDefinition.objects.all()
    serializer_class = serializers.EventDefinition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.EventDefinition
    ordering_fields = "__all__"


class Evidence(viewsets.ModelViewSet):
    queryset = models.Evidence.objects.all()
    serializer_class = serializers.Evidence
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Evidence
    ordering_fields = "__all__"


class EvidenceVariable(viewsets.ModelViewSet):
    queryset = models.EvidenceVariable.objects.all()
    serializer_class = serializers.EvidenceVariable
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.EvidenceVariable
    ordering_fields = "__all__"


class EvidenceVariable_Characteristic(viewsets.ModelViewSet):
    queryset = models.EvidenceVariable_Characteristic.objects.all()
    serializer_class = serializers.EvidenceVariable_Characteristic
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.EvidenceVariable_Characteristic
    ordering_fields = "__all__"
    search_fields = [
        "$definitionCanonical",
        "$participantEffectiveDateTime",
    ]


class ExampleScenario(viewsets.ModelViewSet):
    queryset = models.ExampleScenario.objects.all()
    serializer_class = serializers.ExampleScenario
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExampleScenario
    ordering_fields = "__all__"


class ExampleScenario_Actor(viewsets.ModelViewSet):
    queryset = models.ExampleScenario_Actor.objects.all()
    serializer_class = serializers.ExampleScenario_Actor
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExampleScenario_Actor
    ordering_fields = "__all__"


class ExampleScenario_Instance(viewsets.ModelViewSet):
    queryset = models.ExampleScenario_Instance.objects.all()
    serializer_class = serializers.ExampleScenario_Instance
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExampleScenario_Instance
    ordering_fields = "__all__"


class ExampleScenario_Version(viewsets.ModelViewSet):
    queryset = models.ExampleScenario_Version.objects.all()
    serializer_class = serializers.ExampleScenario_Version
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExampleScenario_Version
    ordering_fields = "__all__"


class ExampleScenario_ContainedInstance(viewsets.ModelViewSet):
    queryset = models.ExampleScenario_ContainedInstance.objects.all()
    serializer_class = serializers.ExampleScenario_ContainedInstance
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExampleScenario_ContainedInstance
    ordering_fields = "__all__"


class ExampleScenario_Process(viewsets.ModelViewSet):
    queryset = models.ExampleScenario_Process.objects.all()
    serializer_class = serializers.ExampleScenario_Process
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExampleScenario_Process
    ordering_fields = "__all__"


class ExampleScenario_Step(viewsets.ModelViewSet):
    queryset = models.ExampleScenario_Step.objects.all()
    serializer_class = serializers.ExampleScenario_Step
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExampleScenario_Step
    ordering_fields = "__all__"


class ExampleScenario_Operation(viewsets.ModelViewSet):
    queryset = models.ExampleScenario_Operation.objects.all()
    serializer_class = serializers.ExampleScenario_Operation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExampleScenario_Operation
    ordering_fields = "__all__"


class ExampleScenario_Alternative(viewsets.ModelViewSet):
    queryset = models.ExampleScenario_Alternative.objects.all()
    serializer_class = serializers.ExampleScenario_Alternative
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExampleScenario_Alternative
    ordering_fields = "__all__"


class ExplanationOfBenefit(viewsets.ModelViewSet):
    queryset = models.ExplanationOfBenefit.objects.all()
    serializer_class = serializers.ExplanationOfBenefit
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExplanationOfBenefit
    ordering_fields = "__all__"


class ExplanationOfBenefit_Related(viewsets.ModelViewSet):
    queryset = models.ExplanationOfBenefit_Related.objects.all()
    serializer_class = serializers.ExplanationOfBenefit_Related
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExplanationOfBenefit_Related
    ordering_fields = "__all__"


class ExplanationOfBenefit_Payee(viewsets.ModelViewSet):
    queryset = models.ExplanationOfBenefit_Payee.objects.all()
    serializer_class = serializers.ExplanationOfBenefit_Payee
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExplanationOfBenefit_Payee
    ordering_fields = "__all__"


class ExplanationOfBenefit_CareTeam(viewsets.ModelViewSet):
    queryset = models.ExplanationOfBenefit_CareTeam.objects.all()
    serializer_class = serializers.ExplanationOfBenefit_CareTeam
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExplanationOfBenefit_CareTeam
    ordering_fields = "__all__"


class ExplanationOfBenefit_SupportingInfo(viewsets.ModelViewSet):
    queryset = models.ExplanationOfBenefit_SupportingInfo.objects.all()
    serializer_class = serializers.ExplanationOfBenefit_SupportingInfo
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExplanationOfBenefit_SupportingInfo
    ordering_fields = "__all__"
    search_fields = [
        "$timingDate",
        "$valueString",
    ]


class ExplanationOfBenefit_Diagnosis(viewsets.ModelViewSet):
    queryset = models.ExplanationOfBenefit_Diagnosis.objects.all()
    serializer_class = serializers.ExplanationOfBenefit_Diagnosis
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExplanationOfBenefit_Diagnosis
    ordering_fields = "__all__"


class ExplanationOfBenefit_Procedure(viewsets.ModelViewSet):
    queryset = models.ExplanationOfBenefit_Procedure.objects.all()
    serializer_class = serializers.ExplanationOfBenefit_Procedure
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExplanationOfBenefit_Procedure
    ordering_fields = "__all__"


class ExplanationOfBenefit_Insurance(viewsets.ModelViewSet):
    queryset = models.ExplanationOfBenefit_Insurance.objects.all()
    serializer_class = serializers.ExplanationOfBenefit_Insurance
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExplanationOfBenefit_Insurance
    ordering_fields = "__all__"


class ExplanationOfBenefit_Accident(viewsets.ModelViewSet):
    queryset = models.ExplanationOfBenefit_Accident.objects.all()
    serializer_class = serializers.ExplanationOfBenefit_Accident
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExplanationOfBenefit_Accident
    ordering_fields = "__all__"


class ExplanationOfBenefit_Item(viewsets.ModelViewSet):
    queryset = models.ExplanationOfBenefit_Item.objects.all()
    serializer_class = serializers.ExplanationOfBenefit_Item
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExplanationOfBenefit_Item
    ordering_fields = "__all__"
    search_fields = [
        "$servicedDate",
    ]


class ExplanationOfBenefit_Adjudication(viewsets.ModelViewSet):
    queryset = models.ExplanationOfBenefit_Adjudication.objects.all()
    serializer_class = serializers.ExplanationOfBenefit_Adjudication
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExplanationOfBenefit_Adjudication
    ordering_fields = "__all__"


class ExplanationOfBenefit_Detail(viewsets.ModelViewSet):
    queryset = models.ExplanationOfBenefit_Detail.objects.all()
    serializer_class = serializers.ExplanationOfBenefit_Detail
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExplanationOfBenefit_Detail
    ordering_fields = "__all__"


class ExplanationOfBenefit_SubDetail(viewsets.ModelViewSet):
    queryset = models.ExplanationOfBenefit_SubDetail.objects.all()
    serializer_class = serializers.ExplanationOfBenefit_SubDetail
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExplanationOfBenefit_SubDetail
    ordering_fields = "__all__"


class ExplanationOfBenefit_AddItem(viewsets.ModelViewSet):
    queryset = models.ExplanationOfBenefit_AddItem.objects.all()
    serializer_class = serializers.ExplanationOfBenefit_AddItem
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExplanationOfBenefit_AddItem
    ordering_fields = "__all__"
    search_fields = [
        "$servicedDate",
    ]


class ExplanationOfBenefit_Detail1(viewsets.ModelViewSet):
    queryset = models.ExplanationOfBenefit_Detail1.objects.all()
    serializer_class = serializers.ExplanationOfBenefit_Detail1
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExplanationOfBenefit_Detail1
    ordering_fields = "__all__"


class ExplanationOfBenefit_SubDetail1(viewsets.ModelViewSet):
    queryset = models.ExplanationOfBenefit_SubDetail1.objects.all()
    serializer_class = serializers.ExplanationOfBenefit_SubDetail1
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExplanationOfBenefit_SubDetail1
    ordering_fields = "__all__"


class ExplanationOfBenefit_Total(viewsets.ModelViewSet):
    queryset = models.ExplanationOfBenefit_Total.objects.all()
    serializer_class = serializers.ExplanationOfBenefit_Total
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExplanationOfBenefit_Total
    ordering_fields = "__all__"


class ExplanationOfBenefit_Payment(viewsets.ModelViewSet):
    queryset = models.ExplanationOfBenefit_Payment.objects.all()
    serializer_class = serializers.ExplanationOfBenefit_Payment
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExplanationOfBenefit_Payment
    ordering_fields = "__all__"


class ExplanationOfBenefit_ProcessNote(viewsets.ModelViewSet):
    queryset = models.ExplanationOfBenefit_ProcessNote.objects.all()
    serializer_class = serializers.ExplanationOfBenefit_ProcessNote
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExplanationOfBenefit_ProcessNote
    ordering_fields = "__all__"


class ExplanationOfBenefit_BenefitBalance(viewsets.ModelViewSet):
    queryset = models.ExplanationOfBenefit_BenefitBalance.objects.all()
    serializer_class = serializers.ExplanationOfBenefit_BenefitBalance
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExplanationOfBenefit_BenefitBalance
    ordering_fields = "__all__"


class ExplanationOfBenefit_Financial(viewsets.ModelViewSet):
    queryset = models.ExplanationOfBenefit_Financial.objects.all()
    serializer_class = serializers.ExplanationOfBenefit_Financial
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ExplanationOfBenefit_Financial
    ordering_fields = "__all__"
    search_fields = [
        "$allowedString",
    ]


class FamilyMemberHistory(viewsets.ModelViewSet):
    queryset = models.FamilyMemberHistory.objects.all()
    serializer_class = serializers.FamilyMemberHistory
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.FamilyMemberHistory
    ordering_fields = "__all__"
    search_fields = [
        "$bornDate",
        "$bornString",
        "$ageString",
        "$deceasedDate",
        "$deceasedString",
    ]


class FamilyMemberHistory_Condition(viewsets.ModelViewSet):
    queryset = models.FamilyMemberHistory_Condition.objects.all()
    serializer_class = serializers.FamilyMemberHistory_Condition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.FamilyMemberHistory_Condition
    ordering_fields = "__all__"
    search_fields = [
        "$onsetString",
    ]


class Flag(viewsets.ModelViewSet):
    queryset = models.Flag.objects.all()
    serializer_class = serializers.Flag
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Flag
    ordering_fields = "__all__"


class Goal(viewsets.ModelViewSet):
    queryset = models.Goal.objects.all()
    serializer_class = serializers.Goal
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Goal
    ordering_fields = "__all__"
    search_fields = [
        "$startDate",
    ]


class Goal_Target(viewsets.ModelViewSet):
    queryset = models.Goal_Target.objects.all()
    serializer_class = serializers.Goal_Target
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Goal_Target
    ordering_fields = "__all__"
    search_fields = [
        "$detailString",
        "$dueDate",
    ]


class GraphDefinition(viewsets.ModelViewSet):
    queryset = models.GraphDefinition.objects.all()
    serializer_class = serializers.GraphDefinition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.GraphDefinition
    ordering_fields = "__all__"


class GraphDefinition_Link(viewsets.ModelViewSet):
    queryset = models.GraphDefinition_Link.objects.all()
    serializer_class = serializers.GraphDefinition_Link
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.GraphDefinition_Link
    ordering_fields = "__all__"


class GraphDefinition_Target(viewsets.ModelViewSet):
    queryset = models.GraphDefinition_Target.objects.all()
    serializer_class = serializers.GraphDefinition_Target
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.GraphDefinition_Target
    ordering_fields = "__all__"


class GraphDefinition_Compartment(viewsets.ModelViewSet):
    queryset = models.GraphDefinition_Compartment.objects.all()
    serializer_class = serializers.GraphDefinition_Compartment
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.GraphDefinition_Compartment
    ordering_fields = "__all__"


class Group(viewsets.ModelViewSet):
    queryset = models.Group.objects.all()
    serializer_class = serializers.Group
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Group
    ordering_fields = "__all__"


class Group_Characteristic(viewsets.ModelViewSet):
    queryset = models.Group_Characteristic.objects.all()
    serializer_class = serializers.Group_Characteristic
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Group_Characteristic
    ordering_fields = "__all__"


class Group_Member(viewsets.ModelViewSet):
    queryset = models.Group_Member.objects.all()
    serializer_class = serializers.Group_Member
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Group_Member
    ordering_fields = "__all__"


class GuidanceResponse(viewsets.ModelViewSet):
    queryset = models.GuidanceResponse.objects.all()
    serializer_class = serializers.GuidanceResponse
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.GuidanceResponse
    ordering_fields = "__all__"
    search_fields = [
        "$moduleUri",
        "$moduleCanonical",
    ]


class HealthcareService(viewsets.ModelViewSet):
    queryset = models.HealthcareService.objects.all()
    serializer_class = serializers.HealthcareService
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.HealthcareService
    ordering_fields = "__all__"


class HealthcareService_Eligibility(viewsets.ModelViewSet):
    queryset = models.HealthcareService_Eligibility.objects.all()
    serializer_class = serializers.HealthcareService_Eligibility
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.HealthcareService_Eligibility
    ordering_fields = "__all__"


class HealthcareService_AvailableTime(viewsets.ModelViewSet):
    queryset = models.HealthcareService_AvailableTime.objects.all()
    serializer_class = serializers.HealthcareService_AvailableTime
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.HealthcareService_AvailableTime
    ordering_fields = "__all__"


class HealthcareService_NotAvailable(viewsets.ModelViewSet):
    queryset = models.HealthcareService_NotAvailable.objects.all()
    serializer_class = serializers.HealthcareService_NotAvailable
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.HealthcareService_NotAvailable
    ordering_fields = "__all__"


class ImagingStudy(viewsets.ModelViewSet):
    queryset = models.ImagingStudy.objects.all()
    serializer_class = serializers.ImagingStudy
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ImagingStudy
    ordering_fields = "__all__"


class ImagingStudy_Series(viewsets.ModelViewSet):
    queryset = models.ImagingStudy_Series.objects.all()
    serializer_class = serializers.ImagingStudy_Series
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ImagingStudy_Series
    ordering_fields = "__all__"


class ImagingStudy_Performer(viewsets.ModelViewSet):
    queryset = models.ImagingStudy_Performer.objects.all()
    serializer_class = serializers.ImagingStudy_Performer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ImagingStudy_Performer
    ordering_fields = "__all__"


class ImagingStudy_Instance(viewsets.ModelViewSet):
    queryset = models.ImagingStudy_Instance.objects.all()
    serializer_class = serializers.ImagingStudy_Instance
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ImagingStudy_Instance
    ordering_fields = "__all__"


class Immunization(viewsets.ModelViewSet):
    queryset = models.Immunization.objects.all()
    serializer_class = serializers.Immunization
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Immunization
    ordering_fields = "__all__"
    search_fields = [
        "$occurrenceDateTime",
        "$occurrenceString",
    ]


class Immunization_Performer(viewsets.ModelViewSet):
    queryset = models.Immunization_Performer.objects.all()
    serializer_class = serializers.Immunization_Performer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Immunization_Performer
    ordering_fields = "__all__"


class Immunization_Education(viewsets.ModelViewSet):
    queryset = models.Immunization_Education.objects.all()
    serializer_class = serializers.Immunization_Education
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Immunization_Education
    ordering_fields = "__all__"


class Immunization_Reaction(viewsets.ModelViewSet):
    queryset = models.Immunization_Reaction.objects.all()
    serializer_class = serializers.Immunization_Reaction
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Immunization_Reaction
    ordering_fields = "__all__"


class Immunization_ProtocolApplied(viewsets.ModelViewSet):
    queryset = models.Immunization_ProtocolApplied.objects.all()
    serializer_class = serializers.Immunization_ProtocolApplied
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Immunization_ProtocolApplied
    ordering_fields = "__all__"
    search_fields = [
        "$doseNumberString",
        "$seriesDosesString",
    ]


class ImmunizationEvaluation(viewsets.ModelViewSet):
    queryset = models.ImmunizationEvaluation.objects.all()
    serializer_class = serializers.ImmunizationEvaluation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ImmunizationEvaluation
    ordering_fields = "__all__"
    search_fields = [
        "$doseNumberString",
        "$seriesDosesString",
    ]


class ImmunizationRecommendation(viewsets.ModelViewSet):
    queryset = models.ImmunizationRecommendation.objects.all()
    serializer_class = serializers.ImmunizationRecommendation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ImmunizationRecommendation
    ordering_fields = "__all__"


class ImmunizationRecommendation_Recommendation(viewsets.ModelViewSet):
    queryset = models.ImmunizationRecommendation_Recommendation.objects.all()
    serializer_class = serializers.ImmunizationRecommendation_Recommendation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ImmunizationRecommendation_Recommendation
    ordering_fields = "__all__"
    search_fields = [
        "$doseNumberString",
        "$seriesDosesString",
    ]


class ImmunizationRecommendation_DateCriterion(viewsets.ModelViewSet):
    queryset = models.ImmunizationRecommendation_DateCriterion.objects.all()
    serializer_class = serializers.ImmunizationRecommendation_DateCriterion
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ImmunizationRecommendation_DateCriterion
    ordering_fields = "__all__"


class ImplementationGuide(viewsets.ModelViewSet):
    queryset = models.ImplementationGuide.objects.all()
    serializer_class = serializers.ImplementationGuide
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ImplementationGuide
    ordering_fields = "__all__"


class ImplementationGuide_DependsOn(viewsets.ModelViewSet):
    queryset = models.ImplementationGuide_DependsOn.objects.all()
    serializer_class = serializers.ImplementationGuide_DependsOn
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ImplementationGuide_DependsOn
    ordering_fields = "__all__"


class ImplementationGuide_Global(viewsets.ModelViewSet):
    queryset = models.ImplementationGuide_Global.objects.all()
    serializer_class = serializers.ImplementationGuide_Global
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ImplementationGuide_Global
    ordering_fields = "__all__"


class ImplementationGuide_Definition(viewsets.ModelViewSet):
    queryset = models.ImplementationGuide_Definition.objects.all()
    serializer_class = serializers.ImplementationGuide_Definition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ImplementationGuide_Definition
    ordering_fields = "__all__"


class ImplementationGuide_Grouping(viewsets.ModelViewSet):
    queryset = models.ImplementationGuide_Grouping.objects.all()
    serializer_class = serializers.ImplementationGuide_Grouping
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ImplementationGuide_Grouping
    ordering_fields = "__all__"


class ImplementationGuide_Resource(viewsets.ModelViewSet):
    queryset = models.ImplementationGuide_Resource.objects.all()
    serializer_class = serializers.ImplementationGuide_Resource
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ImplementationGuide_Resource
    ordering_fields = "__all__"
    search_fields = [
        "$exampleCanonical",
    ]


class ImplementationGuide_Page(viewsets.ModelViewSet):
    queryset = models.ImplementationGuide_Page.objects.all()
    serializer_class = serializers.ImplementationGuide_Page
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ImplementationGuide_Page
    ordering_fields = "__all__"
    search_fields = [
        "$nameUrl",
    ]


class ImplementationGuide_Parameter(viewsets.ModelViewSet):
    queryset = models.ImplementationGuide_Parameter.objects.all()
    serializer_class = serializers.ImplementationGuide_Parameter
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ImplementationGuide_Parameter
    ordering_fields = "__all__"


class ImplementationGuide_Template(viewsets.ModelViewSet):
    queryset = models.ImplementationGuide_Template.objects.all()
    serializer_class = serializers.ImplementationGuide_Template
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ImplementationGuide_Template
    ordering_fields = "__all__"


class ImplementationGuide_Manifest(viewsets.ModelViewSet):
    queryset = models.ImplementationGuide_Manifest.objects.all()
    serializer_class = serializers.ImplementationGuide_Manifest
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ImplementationGuide_Manifest
    ordering_fields = "__all__"


class ImplementationGuide_Resource1(viewsets.ModelViewSet):
    queryset = models.ImplementationGuide_Resource1.objects.all()
    serializer_class = serializers.ImplementationGuide_Resource1
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ImplementationGuide_Resource1
    ordering_fields = "__all__"
    search_fields = [
        "$exampleCanonical",
    ]


class ImplementationGuide_Page1(viewsets.ModelViewSet):
    queryset = models.ImplementationGuide_Page1.objects.all()
    serializer_class = serializers.ImplementationGuide_Page1
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ImplementationGuide_Page1
    ordering_fields = "__all__"


class InsurancePlan(viewsets.ModelViewSet):
    queryset = models.InsurancePlan.objects.all()
    serializer_class = serializers.InsurancePlan
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.InsurancePlan
    ordering_fields = "__all__"


class InsurancePlan_Contact(viewsets.ModelViewSet):
    queryset = models.InsurancePlan_Contact.objects.all()
    serializer_class = serializers.InsurancePlan_Contact
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.InsurancePlan_Contact
    ordering_fields = "__all__"


class InsurancePlan_Coverage(viewsets.ModelViewSet):
    queryset = models.InsurancePlan_Coverage.objects.all()
    serializer_class = serializers.InsurancePlan_Coverage
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.InsurancePlan_Coverage
    ordering_fields = "__all__"


class InsurancePlan_Benefit(viewsets.ModelViewSet):
    queryset = models.InsurancePlan_Benefit.objects.all()
    serializer_class = serializers.InsurancePlan_Benefit
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.InsurancePlan_Benefit
    ordering_fields = "__all__"


class InsurancePlan_Limit(viewsets.ModelViewSet):
    queryset = models.InsurancePlan_Limit.objects.all()
    serializer_class = serializers.InsurancePlan_Limit
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.InsurancePlan_Limit
    ordering_fields = "__all__"


class InsurancePlan_Plan(viewsets.ModelViewSet):
    queryset = models.InsurancePlan_Plan.objects.all()
    serializer_class = serializers.InsurancePlan_Plan
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.InsurancePlan_Plan
    ordering_fields = "__all__"


class InsurancePlan_GeneralCost(viewsets.ModelViewSet):
    queryset = models.InsurancePlan_GeneralCost.objects.all()
    serializer_class = serializers.InsurancePlan_GeneralCost
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.InsurancePlan_GeneralCost
    ordering_fields = "__all__"


class InsurancePlan_SpecificCost(viewsets.ModelViewSet):
    queryset = models.InsurancePlan_SpecificCost.objects.all()
    serializer_class = serializers.InsurancePlan_SpecificCost
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.InsurancePlan_SpecificCost
    ordering_fields = "__all__"


class InsurancePlan_Benefit1(viewsets.ModelViewSet):
    queryset = models.InsurancePlan_Benefit1.objects.all()
    serializer_class = serializers.InsurancePlan_Benefit1
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.InsurancePlan_Benefit1
    ordering_fields = "__all__"


class InsurancePlan_Cost(viewsets.ModelViewSet):
    queryset = models.InsurancePlan_Cost.objects.all()
    serializer_class = serializers.InsurancePlan_Cost
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.InsurancePlan_Cost
    ordering_fields = "__all__"


class Invoice(viewsets.ModelViewSet):
    queryset = models.Invoice.objects.all()
    serializer_class = serializers.Invoice
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Invoice
    ordering_fields = "__all__"


class Invoice_Participant(viewsets.ModelViewSet):
    queryset = models.Invoice_Participant.objects.all()
    serializer_class = serializers.Invoice_Participant
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Invoice_Participant
    ordering_fields = "__all__"


class Invoice_LineItem(viewsets.ModelViewSet):
    queryset = models.Invoice_LineItem.objects.all()
    serializer_class = serializers.Invoice_LineItem
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Invoice_LineItem
    ordering_fields = "__all__"


class Invoice_PriceComponent(viewsets.ModelViewSet):
    queryset = models.Invoice_PriceComponent.objects.all()
    serializer_class = serializers.Invoice_PriceComponent
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Invoice_PriceComponent
    ordering_fields = "__all__"


class Library(viewsets.ModelViewSet):
    queryset = models.Library.objects.all()
    serializer_class = serializers.Library
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Library
    ordering_fields = "__all__"


class Linkage(viewsets.ModelViewSet):
    queryset = models.Linkage.objects.all()
    serializer_class = serializers.Linkage
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Linkage
    ordering_fields = "__all__"


class Linkage_Item(viewsets.ModelViewSet):
    queryset = models.Linkage_Item.objects.all()
    serializer_class = serializers.Linkage_Item
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Linkage_Item
    ordering_fields = "__all__"


class List(viewsets.ModelViewSet):
    queryset = models.List.objects.all()
    serializer_class = serializers.List
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.List
    ordering_fields = "__all__"


class List_Entry(viewsets.ModelViewSet):
    queryset = models.List_Entry.objects.all()
    serializer_class = serializers.List_Entry
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.List_Entry
    ordering_fields = "__all__"


class Location(viewsets.ModelViewSet):
    queryset = models.Location.objects.all()
    serializer_class = serializers.Location
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Location
    ordering_fields = "__all__"


class Location_Position(viewsets.ModelViewSet):
    queryset = models.Location_Position.objects.all()
    serializer_class = serializers.Location_Position
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Location_Position
    ordering_fields = "__all__"


class Location_HoursOfOperation(viewsets.ModelViewSet):
    queryset = models.Location_HoursOfOperation.objects.all()
    serializer_class = serializers.Location_HoursOfOperation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Location_HoursOfOperation
    ordering_fields = "__all__"


class Measure(viewsets.ModelViewSet):
    queryset = models.Measure.objects.all()
    serializer_class = serializers.Measure
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Measure
    ordering_fields = "__all__"


class Measure_Group(viewsets.ModelViewSet):
    queryset = models.Measure_Group.objects.all()
    serializer_class = serializers.Measure_Group
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Measure_Group
    ordering_fields = "__all__"


class Measure_Population(viewsets.ModelViewSet):
    queryset = models.Measure_Population.objects.all()
    serializer_class = serializers.Measure_Population
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Measure_Population
    ordering_fields = "__all__"


class Measure_Stratifier(viewsets.ModelViewSet):
    queryset = models.Measure_Stratifier.objects.all()
    serializer_class = serializers.Measure_Stratifier
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Measure_Stratifier
    ordering_fields = "__all__"


class Measure_Component(viewsets.ModelViewSet):
    queryset = models.Measure_Component.objects.all()
    serializer_class = serializers.Measure_Component
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Measure_Component
    ordering_fields = "__all__"


class Measure_SupplementalData(viewsets.ModelViewSet):
    queryset = models.Measure_SupplementalData.objects.all()
    serializer_class = serializers.Measure_SupplementalData
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Measure_SupplementalData
    ordering_fields = "__all__"


class MeasureReport(viewsets.ModelViewSet):
    queryset = models.MeasureReport.objects.all()
    serializer_class = serializers.MeasureReport
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MeasureReport
    ordering_fields = "__all__"


class MeasureReport_Group(viewsets.ModelViewSet):
    queryset = models.MeasureReport_Group.objects.all()
    serializer_class = serializers.MeasureReport_Group
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MeasureReport_Group
    ordering_fields = "__all__"


class MeasureReport_Population(viewsets.ModelViewSet):
    queryset = models.MeasureReport_Population.objects.all()
    serializer_class = serializers.MeasureReport_Population
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MeasureReport_Population
    ordering_fields = "__all__"


class MeasureReport_Stratifier(viewsets.ModelViewSet):
    queryset = models.MeasureReport_Stratifier.objects.all()
    serializer_class = serializers.MeasureReport_Stratifier
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MeasureReport_Stratifier
    ordering_fields = "__all__"


class MeasureReport_Stratum(viewsets.ModelViewSet):
    queryset = models.MeasureReport_Stratum.objects.all()
    serializer_class = serializers.MeasureReport_Stratum
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MeasureReport_Stratum
    ordering_fields = "__all__"


class MeasureReport_Component(viewsets.ModelViewSet):
    queryset = models.MeasureReport_Component.objects.all()
    serializer_class = serializers.MeasureReport_Component
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MeasureReport_Component
    ordering_fields = "__all__"


class MeasureReport_Population1(viewsets.ModelViewSet):
    queryset = models.MeasureReport_Population1.objects.all()
    serializer_class = serializers.MeasureReport_Population1
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MeasureReport_Population1
    ordering_fields = "__all__"


class Media(viewsets.ModelViewSet):
    queryset = models.Media.objects.all()
    serializer_class = serializers.Media
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Media
    ordering_fields = "__all__"
    search_fields = [
        "$createdDateTime",
    ]


class Medication(viewsets.ModelViewSet):
    queryset = models.Medication.objects.all()
    serializer_class = serializers.Medication
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Medication
    ordering_fields = "__all__"


class Medication_Ingredient(viewsets.ModelViewSet):
    queryset = models.Medication_Ingredient.objects.all()
    serializer_class = serializers.Medication_Ingredient
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Medication_Ingredient
    ordering_fields = "__all__"


class Medication_Batch(viewsets.ModelViewSet):
    queryset = models.Medication_Batch.objects.all()
    serializer_class = serializers.Medication_Batch
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Medication_Batch
    ordering_fields = "__all__"


class MedicationAdministration(viewsets.ModelViewSet):
    queryset = models.MedicationAdministration.objects.all()
    serializer_class = serializers.MedicationAdministration
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationAdministration
    ordering_fields = "__all__"
    search_fields = [
        "$effectiveDateTime",
    ]


class MedicationAdministration_Performer(viewsets.ModelViewSet):
    queryset = models.MedicationAdministration_Performer.objects.all()
    serializer_class = serializers.MedicationAdministration_Performer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationAdministration_Performer
    ordering_fields = "__all__"


class MedicationAdministration_Dosage(viewsets.ModelViewSet):
    queryset = models.MedicationAdministration_Dosage.objects.all()
    serializer_class = serializers.MedicationAdministration_Dosage
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationAdministration_Dosage
    ordering_fields = "__all__"


class MedicationDispense(viewsets.ModelViewSet):
    queryset = models.MedicationDispense.objects.all()
    serializer_class = serializers.MedicationDispense
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationDispense
    ordering_fields = "__all__"


class MedicationDispense_Performer(viewsets.ModelViewSet):
    queryset = models.MedicationDispense_Performer.objects.all()
    serializer_class = serializers.MedicationDispense_Performer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationDispense_Performer
    ordering_fields = "__all__"


class MedicationDispense_Substitution(viewsets.ModelViewSet):
    queryset = models.MedicationDispense_Substitution.objects.all()
    serializer_class = serializers.MedicationDispense_Substitution
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationDispense_Substitution
    ordering_fields = "__all__"


class MedicationKnowledge(viewsets.ModelViewSet):
    queryset = models.MedicationKnowledge.objects.all()
    serializer_class = serializers.MedicationKnowledge
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationKnowledge
    ordering_fields = "__all__"


class MedicationKnowledge_RelatedMedicationKnowledge(viewsets.ModelViewSet):
    queryset = models.MedicationKnowledge_RelatedMedicationKnowledge.objects.all()
    serializer_class = serializers.MedicationKnowledge_RelatedMedicationKnowledge
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationKnowledge_RelatedMedicationKnowledge
    ordering_fields = "__all__"


class MedicationKnowledge_Monograph(viewsets.ModelViewSet):
    queryset = models.MedicationKnowledge_Monograph.objects.all()
    serializer_class = serializers.MedicationKnowledge_Monograph
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationKnowledge_Monograph
    ordering_fields = "__all__"


class MedicationKnowledge_Ingredient(viewsets.ModelViewSet):
    queryset = models.MedicationKnowledge_Ingredient.objects.all()
    serializer_class = serializers.MedicationKnowledge_Ingredient
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationKnowledge_Ingredient
    ordering_fields = "__all__"


class MedicationKnowledge_Cost(viewsets.ModelViewSet):
    queryset = models.MedicationKnowledge_Cost.objects.all()
    serializer_class = serializers.MedicationKnowledge_Cost
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationKnowledge_Cost
    ordering_fields = "__all__"


class MedicationKnowledge_MonitoringProgram(viewsets.ModelViewSet):
    queryset = models.MedicationKnowledge_MonitoringProgram.objects.all()
    serializer_class = serializers.MedicationKnowledge_MonitoringProgram
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationKnowledge_MonitoringProgram
    ordering_fields = "__all__"


class MedicationKnowledge_AdministrationGuidelines(viewsets.ModelViewSet):
    queryset = models.MedicationKnowledge_AdministrationGuidelines.objects.all()
    serializer_class = serializers.MedicationKnowledge_AdministrationGuidelines
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationKnowledge_AdministrationGuidelines
    ordering_fields = "__all__"


class MedicationKnowledge_Dosage(viewsets.ModelViewSet):
    queryset = models.MedicationKnowledge_Dosage.objects.all()
    serializer_class = serializers.MedicationKnowledge_Dosage
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationKnowledge_Dosage
    ordering_fields = "__all__"


class MedicationKnowledge_PatientCharacteristics(viewsets.ModelViewSet):
    queryset = models.MedicationKnowledge_PatientCharacteristics.objects.all()
    serializer_class = serializers.MedicationKnowledge_PatientCharacteristics
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationKnowledge_PatientCharacteristics
    ordering_fields = "__all__"


class MedicationKnowledge_MedicineClassification(viewsets.ModelViewSet):
    queryset = models.MedicationKnowledge_MedicineClassification.objects.all()
    serializer_class = serializers.MedicationKnowledge_MedicineClassification
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationKnowledge_MedicineClassification
    ordering_fields = "__all__"


class MedicationKnowledge_Packaging(viewsets.ModelViewSet):
    queryset = models.MedicationKnowledge_Packaging.objects.all()
    serializer_class = serializers.MedicationKnowledge_Packaging
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationKnowledge_Packaging
    ordering_fields = "__all__"


class MedicationKnowledge_DrugCharacteristic(viewsets.ModelViewSet):
    queryset = models.MedicationKnowledge_DrugCharacteristic.objects.all()
    serializer_class = serializers.MedicationKnowledge_DrugCharacteristic
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationKnowledge_DrugCharacteristic
    ordering_fields = "__all__"
    search_fields = [
        "$valueString",
        "$valueBase64Binary",
    ]


class MedicationKnowledge_Regulatory(viewsets.ModelViewSet):
    queryset = models.MedicationKnowledge_Regulatory.objects.all()
    serializer_class = serializers.MedicationKnowledge_Regulatory
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationKnowledge_Regulatory
    ordering_fields = "__all__"


class MedicationKnowledge_Substitution(viewsets.ModelViewSet):
    queryset = models.MedicationKnowledge_Substitution.objects.all()
    serializer_class = serializers.MedicationKnowledge_Substitution
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationKnowledge_Substitution
    ordering_fields = "__all__"


class MedicationKnowledge_Schedule(viewsets.ModelViewSet):
    queryset = models.MedicationKnowledge_Schedule.objects.all()
    serializer_class = serializers.MedicationKnowledge_Schedule
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationKnowledge_Schedule
    ordering_fields = "__all__"


class MedicationKnowledge_MaxDispense(viewsets.ModelViewSet):
    queryset = models.MedicationKnowledge_MaxDispense.objects.all()
    serializer_class = serializers.MedicationKnowledge_MaxDispense
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationKnowledge_MaxDispense
    ordering_fields = "__all__"


class MedicationKnowledge_Kinetics(viewsets.ModelViewSet):
    queryset = models.MedicationKnowledge_Kinetics.objects.all()
    serializer_class = serializers.MedicationKnowledge_Kinetics
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationKnowledge_Kinetics
    ordering_fields = "__all__"


class MedicationRequest(viewsets.ModelViewSet):
    queryset = models.MedicationRequest.objects.all()
    serializer_class = serializers.MedicationRequest
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationRequest
    ordering_fields = "__all__"


class MedicationRequest_DispenseRequest(viewsets.ModelViewSet):
    queryset = models.MedicationRequest_DispenseRequest.objects.all()
    serializer_class = serializers.MedicationRequest_DispenseRequest
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationRequest_DispenseRequest
    ordering_fields = "__all__"


class MedicationRequest_InitialFill(viewsets.ModelViewSet):
    queryset = models.MedicationRequest_InitialFill.objects.all()
    serializer_class = serializers.MedicationRequest_InitialFill
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationRequest_InitialFill
    ordering_fields = "__all__"


class MedicationRequest_Substitution(viewsets.ModelViewSet):
    queryset = models.MedicationRequest_Substitution.objects.all()
    serializer_class = serializers.MedicationRequest_Substitution
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationRequest_Substitution
    ordering_fields = "__all__"


class MedicationStatement(viewsets.ModelViewSet):
    queryset = models.MedicationStatement.objects.all()
    serializer_class = serializers.MedicationStatement
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicationStatement
    ordering_fields = "__all__"
    search_fields = [
        "$effectiveDateTime",
    ]


class MedicinalProduct(viewsets.ModelViewSet):
    queryset = models.MedicinalProduct.objects.all()
    serializer_class = serializers.MedicinalProduct
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProduct
    ordering_fields = "__all__"


class MedicinalProduct_Name(viewsets.ModelViewSet):
    queryset = models.MedicinalProduct_Name.objects.all()
    serializer_class = serializers.MedicinalProduct_Name
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProduct_Name
    ordering_fields = "__all__"


class MedicinalProduct_NamePart(viewsets.ModelViewSet):
    queryset = models.MedicinalProduct_NamePart.objects.all()
    serializer_class = serializers.MedicinalProduct_NamePart
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProduct_NamePart
    ordering_fields = "__all__"


class MedicinalProduct_CountryLanguage(viewsets.ModelViewSet):
    queryset = models.MedicinalProduct_CountryLanguage.objects.all()
    serializer_class = serializers.MedicinalProduct_CountryLanguage
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProduct_CountryLanguage
    ordering_fields = "__all__"


class MedicinalProduct_ManufacturingBusinessOperation(viewsets.ModelViewSet):
    queryset = models.MedicinalProduct_ManufacturingBusinessOperation.objects.all()
    serializer_class = serializers.MedicinalProduct_ManufacturingBusinessOperation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProduct_ManufacturingBusinessOperation
    ordering_fields = "__all__"


class MedicinalProduct_SpecialDesignation(viewsets.ModelViewSet):
    queryset = models.MedicinalProduct_SpecialDesignation.objects.all()
    serializer_class = serializers.MedicinalProduct_SpecialDesignation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProduct_SpecialDesignation
    ordering_fields = "__all__"


class MedicinalProductAuthorization(viewsets.ModelViewSet):
    queryset = models.MedicinalProductAuthorization.objects.all()
    serializer_class = serializers.MedicinalProductAuthorization
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductAuthorization
    ordering_fields = "__all__"


class MedicinalProductAuthorization_JurisdictionalAuthorization(viewsets.ModelViewSet):
    queryset = models.MedicinalProductAuthorization_JurisdictionalAuthorization.objects.all()
    serializer_class = serializers.MedicinalProductAuthorization_JurisdictionalAuthorization
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductAuthorization_JurisdictionalAuthorization
    ordering_fields = "__all__"


class MedicinalProductAuthorization_Procedure(viewsets.ModelViewSet):
    queryset = models.MedicinalProductAuthorization_Procedure.objects.all()
    serializer_class = serializers.MedicinalProductAuthorization_Procedure
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductAuthorization_Procedure
    ordering_fields = "__all__"
    search_fields = [
        "$dateDateTime",
    ]


class MedicinalProductContraindication(viewsets.ModelViewSet):
    queryset = models.MedicinalProductContraindication.objects.all()
    serializer_class = serializers.MedicinalProductContraindication
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductContraindication
    ordering_fields = "__all__"


class MedicinalProductContraindication_OtherTherapy(viewsets.ModelViewSet):
    queryset = models.MedicinalProductContraindication_OtherTherapy.objects.all()
    serializer_class = serializers.MedicinalProductContraindication_OtherTherapy
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductContraindication_OtherTherapy
    ordering_fields = "__all__"


class MedicinalProductIndication(viewsets.ModelViewSet):
    queryset = models.MedicinalProductIndication.objects.all()
    serializer_class = serializers.MedicinalProductIndication
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductIndication
    ordering_fields = "__all__"


class MedicinalProductIndication_OtherTherapy(viewsets.ModelViewSet):
    queryset = models.MedicinalProductIndication_OtherTherapy.objects.all()
    serializer_class = serializers.MedicinalProductIndication_OtherTherapy
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductIndication_OtherTherapy
    ordering_fields = "__all__"


class MedicinalProductIngredient(viewsets.ModelViewSet):
    queryset = models.MedicinalProductIngredient.objects.all()
    serializer_class = serializers.MedicinalProductIngredient
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductIngredient
    ordering_fields = "__all__"


class MedicinalProductIngredient_SpecifiedSubstance(viewsets.ModelViewSet):
    queryset = models.MedicinalProductIngredient_SpecifiedSubstance.objects.all()
    serializer_class = serializers.MedicinalProductIngredient_SpecifiedSubstance
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductIngredient_SpecifiedSubstance
    ordering_fields = "__all__"


class MedicinalProductIngredient_Strength(viewsets.ModelViewSet):
    queryset = models.MedicinalProductIngredient_Strength.objects.all()
    serializer_class = serializers.MedicinalProductIngredient_Strength
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductIngredient_Strength
    ordering_fields = "__all__"


class MedicinalProductIngredient_ReferenceStrength(viewsets.ModelViewSet):
    queryset = models.MedicinalProductIngredient_ReferenceStrength.objects.all()
    serializer_class = serializers.MedicinalProductIngredient_ReferenceStrength
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductIngredient_ReferenceStrength
    ordering_fields = "__all__"


class MedicinalProductIngredient_Substance(viewsets.ModelViewSet):
    queryset = models.MedicinalProductIngredient_Substance.objects.all()
    serializer_class = serializers.MedicinalProductIngredient_Substance
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductIngredient_Substance
    ordering_fields = "__all__"


class MedicinalProductInteraction(viewsets.ModelViewSet):
    queryset = models.MedicinalProductInteraction.objects.all()
    serializer_class = serializers.MedicinalProductInteraction
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductInteraction
    ordering_fields = "__all__"


class MedicinalProductInteraction_Interactant(viewsets.ModelViewSet):
    queryset = models.MedicinalProductInteraction_Interactant.objects.all()
    serializer_class = serializers.MedicinalProductInteraction_Interactant
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductInteraction_Interactant
    ordering_fields = "__all__"


class MedicinalProductManufactured(viewsets.ModelViewSet):
    queryset = models.MedicinalProductManufactured.objects.all()
    serializer_class = serializers.MedicinalProductManufactured
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductManufactured
    ordering_fields = "__all__"


class MedicinalProductPackaged(viewsets.ModelViewSet):
    queryset = models.MedicinalProductPackaged.objects.all()
    serializer_class = serializers.MedicinalProductPackaged
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductPackaged
    ordering_fields = "__all__"


class MedicinalProductPackaged_BatchIdentifier(viewsets.ModelViewSet):
    queryset = models.MedicinalProductPackaged_BatchIdentifier.objects.all()
    serializer_class = serializers.MedicinalProductPackaged_BatchIdentifier
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductPackaged_BatchIdentifier
    ordering_fields = "__all__"


class MedicinalProductPackaged_PackageItem(viewsets.ModelViewSet):
    queryset = models.MedicinalProductPackaged_PackageItem.objects.all()
    serializer_class = serializers.MedicinalProductPackaged_PackageItem
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductPackaged_PackageItem
    ordering_fields = "__all__"


class MedicinalProductPharmaceutical(viewsets.ModelViewSet):
    queryset = models.MedicinalProductPharmaceutical.objects.all()
    serializer_class = serializers.MedicinalProductPharmaceutical
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductPharmaceutical
    ordering_fields = "__all__"


class MedicinalProductPharmaceutical_Characteristics(viewsets.ModelViewSet):
    queryset = models.MedicinalProductPharmaceutical_Characteristics.objects.all()
    serializer_class = serializers.MedicinalProductPharmaceutical_Characteristics
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductPharmaceutical_Characteristics
    ordering_fields = "__all__"


class MedicinalProductPharmaceutical_RouteOfAdministration(viewsets.ModelViewSet):
    queryset = models.MedicinalProductPharmaceutical_RouteOfAdministration.objects.all()
    serializer_class = serializers.MedicinalProductPharmaceutical_RouteOfAdministration
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductPharmaceutical_RouteOfAdministration
    ordering_fields = "__all__"


class MedicinalProductPharmaceutical_TargetSpecies(viewsets.ModelViewSet):
    queryset = models.MedicinalProductPharmaceutical_TargetSpecies.objects.all()
    serializer_class = serializers.MedicinalProductPharmaceutical_TargetSpecies
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductPharmaceutical_TargetSpecies
    ordering_fields = "__all__"


class MedicinalProductPharmaceutical_WithdrawalPeriod(viewsets.ModelViewSet):
    queryset = models.MedicinalProductPharmaceutical_WithdrawalPeriod.objects.all()
    serializer_class = serializers.MedicinalProductPharmaceutical_WithdrawalPeriod
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductPharmaceutical_WithdrawalPeriod
    ordering_fields = "__all__"


class MedicinalProductUndesirableEffect(viewsets.ModelViewSet):
    queryset = models.MedicinalProductUndesirableEffect.objects.all()
    serializer_class = serializers.MedicinalProductUndesirableEffect
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MedicinalProductUndesirableEffect
    ordering_fields = "__all__"


class MessageDefinition(viewsets.ModelViewSet):
    queryset = models.MessageDefinition.objects.all()
    serializer_class = serializers.MessageDefinition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MessageDefinition
    ordering_fields = "__all__"
    search_fields = [
        "$eventUri",
    ]


class MessageDefinition_Focus(viewsets.ModelViewSet):
    queryset = models.MessageDefinition_Focus.objects.all()
    serializer_class = serializers.MessageDefinition_Focus
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MessageDefinition_Focus
    ordering_fields = "__all__"


class MessageDefinition_AllowedResponse(viewsets.ModelViewSet):
    queryset = models.MessageDefinition_AllowedResponse.objects.all()
    serializer_class = serializers.MessageDefinition_AllowedResponse
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MessageDefinition_AllowedResponse
    ordering_fields = "__all__"


class MessageHeader(viewsets.ModelViewSet):
    queryset = models.MessageHeader.objects.all()
    serializer_class = serializers.MessageHeader
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MessageHeader
    ordering_fields = "__all__"
    search_fields = [
        "$eventUri",
    ]


class MessageHeader_Destination(viewsets.ModelViewSet):
    queryset = models.MessageHeader_Destination.objects.all()
    serializer_class = serializers.MessageHeader_Destination
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MessageHeader_Destination
    ordering_fields = "__all__"


class MessageHeader_Source(viewsets.ModelViewSet):
    queryset = models.MessageHeader_Source.objects.all()
    serializer_class = serializers.MessageHeader_Source
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MessageHeader_Source
    ordering_fields = "__all__"


class MessageHeader_Response(viewsets.ModelViewSet):
    queryset = models.MessageHeader_Response.objects.all()
    serializer_class = serializers.MessageHeader_Response
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MessageHeader_Response
    ordering_fields = "__all__"


class MolecularSequence(viewsets.ModelViewSet):
    queryset = models.MolecularSequence.objects.all()
    serializer_class = serializers.MolecularSequence
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MolecularSequence
    ordering_fields = "__all__"


class MolecularSequence_ReferenceSeq(viewsets.ModelViewSet):
    queryset = models.MolecularSequence_ReferenceSeq.objects.all()
    serializer_class = serializers.MolecularSequence_ReferenceSeq
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MolecularSequence_ReferenceSeq
    ordering_fields = "__all__"


class MolecularSequence_Variant(viewsets.ModelViewSet):
    queryset = models.MolecularSequence_Variant.objects.all()
    serializer_class = serializers.MolecularSequence_Variant
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MolecularSequence_Variant
    ordering_fields = "__all__"


class MolecularSequence_Quality(viewsets.ModelViewSet):
    queryset = models.MolecularSequence_Quality.objects.all()
    serializer_class = serializers.MolecularSequence_Quality
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MolecularSequence_Quality
    ordering_fields = "__all__"


class MolecularSequence_Roc(viewsets.ModelViewSet):
    queryset = models.MolecularSequence_Roc.objects.all()
    serializer_class = serializers.MolecularSequence_Roc
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MolecularSequence_Roc
    ordering_fields = "__all__"


class MolecularSequence_Repository(viewsets.ModelViewSet):
    queryset = models.MolecularSequence_Repository.objects.all()
    serializer_class = serializers.MolecularSequence_Repository
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MolecularSequence_Repository
    ordering_fields = "__all__"


class MolecularSequence_StructureVariant(viewsets.ModelViewSet):
    queryset = models.MolecularSequence_StructureVariant.objects.all()
    serializer_class = serializers.MolecularSequence_StructureVariant
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MolecularSequence_StructureVariant
    ordering_fields = "__all__"


class MolecularSequence_Outer(viewsets.ModelViewSet):
    queryset = models.MolecularSequence_Outer.objects.all()
    serializer_class = serializers.MolecularSequence_Outer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MolecularSequence_Outer
    ordering_fields = "__all__"


class MolecularSequence_Inner(viewsets.ModelViewSet):
    queryset = models.MolecularSequence_Inner.objects.all()
    serializer_class = serializers.MolecularSequence_Inner
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.MolecularSequence_Inner
    ordering_fields = "__all__"


class NamingSystem(viewsets.ModelViewSet):
    queryset = models.NamingSystem.objects.all()
    serializer_class = serializers.NamingSystem
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.NamingSystem
    ordering_fields = "__all__"


class NamingSystem_UniqueId(viewsets.ModelViewSet):
    queryset = models.NamingSystem_UniqueId.objects.all()
    serializer_class = serializers.NamingSystem_UniqueId
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.NamingSystem_UniqueId
    ordering_fields = "__all__"


class NutritionOrder(viewsets.ModelViewSet):
    queryset = models.NutritionOrder.objects.all()
    serializer_class = serializers.NutritionOrder
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.NutritionOrder
    ordering_fields = "__all__"


class NutritionOrder_OralDiet(viewsets.ModelViewSet):
    queryset = models.NutritionOrder_OralDiet.objects.all()
    serializer_class = serializers.NutritionOrder_OralDiet
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.NutritionOrder_OralDiet
    ordering_fields = "__all__"


class NutritionOrder_Nutrient(viewsets.ModelViewSet):
    queryset = models.NutritionOrder_Nutrient.objects.all()
    serializer_class = serializers.NutritionOrder_Nutrient
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.NutritionOrder_Nutrient
    ordering_fields = "__all__"


class NutritionOrder_Texture(viewsets.ModelViewSet):
    queryset = models.NutritionOrder_Texture.objects.all()
    serializer_class = serializers.NutritionOrder_Texture
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.NutritionOrder_Texture
    ordering_fields = "__all__"


class NutritionOrder_Supplement(viewsets.ModelViewSet):
    queryset = models.NutritionOrder_Supplement.objects.all()
    serializer_class = serializers.NutritionOrder_Supplement
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.NutritionOrder_Supplement
    ordering_fields = "__all__"


class NutritionOrder_EnteralFormula(viewsets.ModelViewSet):
    queryset = models.NutritionOrder_EnteralFormula.objects.all()
    serializer_class = serializers.NutritionOrder_EnteralFormula
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.NutritionOrder_EnteralFormula
    ordering_fields = "__all__"


class NutritionOrder_Administration(viewsets.ModelViewSet):
    queryset = models.NutritionOrder_Administration.objects.all()
    serializer_class = serializers.NutritionOrder_Administration
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.NutritionOrder_Administration
    ordering_fields = "__all__"


class Observation(viewsets.ModelViewSet):
    queryset = models.Observation.objects.all()
    serializer_class = serializers.Observation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Observation
    ordering_fields = "__all__"
    search_fields = [
        "$effectiveDateTime",
        "$effectiveInstant",
        "$valueString",
        "$valueTime",
        "$valueDateTime",
    ]


class Observation_ReferenceRange(viewsets.ModelViewSet):
    queryset = models.Observation_ReferenceRange.objects.all()
    serializer_class = serializers.Observation_ReferenceRange
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Observation_ReferenceRange
    ordering_fields = "__all__"


class Observation_Component(viewsets.ModelViewSet):
    queryset = models.Observation_Component.objects.all()
    serializer_class = serializers.Observation_Component
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Observation_Component
    ordering_fields = "__all__"
    search_fields = [
        "$valueString",
        "$valueTime",
        "$valueDateTime",
    ]


class ObservationDefinition(viewsets.ModelViewSet):
    queryset = models.ObservationDefinition.objects.all()
    serializer_class = serializers.ObservationDefinition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ObservationDefinition
    ordering_fields = "__all__"


class ObservationDefinition_QuantitativeDetails(viewsets.ModelViewSet):
    queryset = models.ObservationDefinition_QuantitativeDetails.objects.all()
    serializer_class = serializers.ObservationDefinition_QuantitativeDetails
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ObservationDefinition_QuantitativeDetails
    ordering_fields = "__all__"


class ObservationDefinition_QualifiedInterval(viewsets.ModelViewSet):
    queryset = models.ObservationDefinition_QualifiedInterval.objects.all()
    serializer_class = serializers.ObservationDefinition_QualifiedInterval
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ObservationDefinition_QualifiedInterval
    ordering_fields = "__all__"


class OperationDefinition(viewsets.ModelViewSet):
    queryset = models.OperationDefinition.objects.all()
    serializer_class = serializers.OperationDefinition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.OperationDefinition
    ordering_fields = "__all__"


class OperationDefinition_Parameter(viewsets.ModelViewSet):
    queryset = models.OperationDefinition_Parameter.objects.all()
    serializer_class = serializers.OperationDefinition_Parameter
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.OperationDefinition_Parameter
    ordering_fields = "__all__"


class OperationDefinition_Binding(viewsets.ModelViewSet):
    queryset = models.OperationDefinition_Binding.objects.all()
    serializer_class = serializers.OperationDefinition_Binding
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.OperationDefinition_Binding
    ordering_fields = "__all__"


class OperationDefinition_ReferencedFrom(viewsets.ModelViewSet):
    queryset = models.OperationDefinition_ReferencedFrom.objects.all()
    serializer_class = serializers.OperationDefinition_ReferencedFrom
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.OperationDefinition_ReferencedFrom
    ordering_fields = "__all__"


class OperationDefinition_Overload(viewsets.ModelViewSet):
    queryset = models.OperationDefinition_Overload.objects.all()
    serializer_class = serializers.OperationDefinition_Overload
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.OperationDefinition_Overload
    ordering_fields = "__all__"


class OperationOutcome(viewsets.ModelViewSet):
    queryset = models.OperationOutcome.objects.all()
    serializer_class = serializers.OperationOutcome
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.OperationOutcome
    ordering_fields = "__all__"


class OperationOutcome_Issue(viewsets.ModelViewSet):
    queryset = models.OperationOutcome_Issue.objects.all()
    serializer_class = serializers.OperationOutcome_Issue
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.OperationOutcome_Issue
    ordering_fields = "__all__"


class Organization(viewsets.ModelViewSet):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.Organization
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Organization
    ordering_fields = "__all__"


class Organization_Contact(viewsets.ModelViewSet):
    queryset = models.Organization_Contact.objects.all()
    serializer_class = serializers.Organization_Contact
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Organization_Contact
    ordering_fields = "__all__"


class OrganizationAffiliation(viewsets.ModelViewSet):
    queryset = models.OrganizationAffiliation.objects.all()
    serializer_class = serializers.OrganizationAffiliation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.OrganizationAffiliation
    ordering_fields = "__all__"


class Parameters(viewsets.ModelViewSet):
    queryset = models.Parameters.objects.all()
    serializer_class = serializers.Parameters
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Parameters
    ordering_fields = "__all__"


class Parameters_Parameter(viewsets.ModelViewSet):
    queryset = models.Parameters_Parameter.objects.all()
    serializer_class = serializers.Parameters_Parameter
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Parameters_Parameter
    ordering_fields = "__all__"
    search_fields = [
        "$valueBase64Binary",
        "$valueCanonical",
        "$valueCode",
        "$valueDate",
        "$valueDateTime",
        "$valueId",
        "$valueInstant",
        "$valueMarkdown",
        "$valueOid",
        "$valueString",
        "$valueTime",
        "$valueUri",
        "$valueUrl",
        "$valueUuid",
    ]


class Patient(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.Patient
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Patient
    ordering_fields = "__all__"
    search_fields = [
        "$deceasedDateTime",
    ]


class Patient_Contact(viewsets.ModelViewSet):
    queryset = models.Patient_Contact.objects.all()
    serializer_class = serializers.Patient_Contact
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Patient_Contact
    ordering_fields = "__all__"


class Patient_Communication(viewsets.ModelViewSet):
    queryset = models.Patient_Communication.objects.all()
    serializer_class = serializers.Patient_Communication
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Patient_Communication
    ordering_fields = "__all__"


class Patient_Link(viewsets.ModelViewSet):
    queryset = models.Patient_Link.objects.all()
    serializer_class = serializers.Patient_Link
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Patient_Link
    ordering_fields = "__all__"


class PaymentNotice(viewsets.ModelViewSet):
    queryset = models.PaymentNotice.objects.all()
    serializer_class = serializers.PaymentNotice
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.PaymentNotice
    ordering_fields = "__all__"


class PaymentReconciliation(viewsets.ModelViewSet):
    queryset = models.PaymentReconciliation.objects.all()
    serializer_class = serializers.PaymentReconciliation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.PaymentReconciliation
    ordering_fields = "__all__"


class PaymentReconciliation_Detail(viewsets.ModelViewSet):
    queryset = models.PaymentReconciliation_Detail.objects.all()
    serializer_class = serializers.PaymentReconciliation_Detail
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.PaymentReconciliation_Detail
    ordering_fields = "__all__"


class PaymentReconciliation_ProcessNote(viewsets.ModelViewSet):
    queryset = models.PaymentReconciliation_ProcessNote.objects.all()
    serializer_class = serializers.PaymentReconciliation_ProcessNote
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.PaymentReconciliation_ProcessNote
    ordering_fields = "__all__"


class Person(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.Person
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Person
    ordering_fields = "__all__"


class Person_Link(viewsets.ModelViewSet):
    queryset = models.Person_Link.objects.all()
    serializer_class = serializers.Person_Link
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Person_Link
    ordering_fields = "__all__"


class PlanDefinition(viewsets.ModelViewSet):
    queryset = models.PlanDefinition.objects.all()
    serializer_class = serializers.PlanDefinition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.PlanDefinition
    ordering_fields = "__all__"


class PlanDefinition_Goal(viewsets.ModelViewSet):
    queryset = models.PlanDefinition_Goal.objects.all()
    serializer_class = serializers.PlanDefinition_Goal
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.PlanDefinition_Goal
    ordering_fields = "__all__"


class PlanDefinition_Target(viewsets.ModelViewSet):
    queryset = models.PlanDefinition_Target.objects.all()
    serializer_class = serializers.PlanDefinition_Target
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.PlanDefinition_Target
    ordering_fields = "__all__"


class PlanDefinition_Action(viewsets.ModelViewSet):
    queryset = models.PlanDefinition_Action.objects.all()
    serializer_class = serializers.PlanDefinition_Action
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.PlanDefinition_Action
    ordering_fields = "__all__"
    search_fields = [
        "$timingDateTime",
        "$definitionCanonical",
        "$definitionUri",
    ]


class PlanDefinition_Condition(viewsets.ModelViewSet):
    queryset = models.PlanDefinition_Condition.objects.all()
    serializer_class = serializers.PlanDefinition_Condition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.PlanDefinition_Condition
    ordering_fields = "__all__"


class PlanDefinition_RelatedAction(viewsets.ModelViewSet):
    queryset = models.PlanDefinition_RelatedAction.objects.all()
    serializer_class = serializers.PlanDefinition_RelatedAction
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.PlanDefinition_RelatedAction
    ordering_fields = "__all__"


class PlanDefinition_Participant(viewsets.ModelViewSet):
    queryset = models.PlanDefinition_Participant.objects.all()
    serializer_class = serializers.PlanDefinition_Participant
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.PlanDefinition_Participant
    ordering_fields = "__all__"


class PlanDefinition_DynamicValue(viewsets.ModelViewSet):
    queryset = models.PlanDefinition_DynamicValue.objects.all()
    serializer_class = serializers.PlanDefinition_DynamicValue
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.PlanDefinition_DynamicValue
    ordering_fields = "__all__"


class Practitioner(viewsets.ModelViewSet):
    queryset = models.Practitioner.objects.all()
    serializer_class = serializers.Practitioner
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Practitioner
    ordering_fields = "__all__"


class Practitioner_Qualification(viewsets.ModelViewSet):
    queryset = models.Practitioner_Qualification.objects.all()
    serializer_class = serializers.Practitioner_Qualification
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Practitioner_Qualification
    ordering_fields = "__all__"


class PractitionerRole(viewsets.ModelViewSet):
    queryset = models.PractitionerRole.objects.all()
    serializer_class = serializers.PractitionerRole
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.PractitionerRole
    ordering_fields = "__all__"


class PractitionerRole_AvailableTime(viewsets.ModelViewSet):
    queryset = models.PractitionerRole_AvailableTime.objects.all()
    serializer_class = serializers.PractitionerRole_AvailableTime
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.PractitionerRole_AvailableTime
    ordering_fields = "__all__"


class PractitionerRole_NotAvailable(viewsets.ModelViewSet):
    queryset = models.PractitionerRole_NotAvailable.objects.all()
    serializer_class = serializers.PractitionerRole_NotAvailable
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.PractitionerRole_NotAvailable
    ordering_fields = "__all__"


class Procedure(viewsets.ModelViewSet):
    queryset = models.Procedure.objects.all()
    serializer_class = serializers.Procedure
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Procedure
    ordering_fields = "__all__"
    search_fields = [
        "$performedDateTime",
        "$performedString",
    ]


class Procedure_Performer(viewsets.ModelViewSet):
    queryset = models.Procedure_Performer.objects.all()
    serializer_class = serializers.Procedure_Performer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Procedure_Performer
    ordering_fields = "__all__"


class Procedure_FocalDevice(viewsets.ModelViewSet):
    queryset = models.Procedure_FocalDevice.objects.all()
    serializer_class = serializers.Procedure_FocalDevice
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Procedure_FocalDevice
    ordering_fields = "__all__"


class Provenance(viewsets.ModelViewSet):
    queryset = models.Provenance.objects.all()
    serializer_class = serializers.Provenance
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Provenance
    ordering_fields = "__all__"
    search_fields = [
        "$occurredDateTime",
    ]


class Provenance_Agent(viewsets.ModelViewSet):
    queryset = models.Provenance_Agent.objects.all()
    serializer_class = serializers.Provenance_Agent
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Provenance_Agent
    ordering_fields = "__all__"


class Provenance_Entity(viewsets.ModelViewSet):
    queryset = models.Provenance_Entity.objects.all()
    serializer_class = serializers.Provenance_Entity
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Provenance_Entity
    ordering_fields = "__all__"


class Questionnaire(viewsets.ModelViewSet):
    queryset = models.Questionnaire.objects.all()
    serializer_class = serializers.Questionnaire
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Questionnaire
    ordering_fields = "__all__"


class Questionnaire_Item(viewsets.ModelViewSet):
    queryset = models.Questionnaire_Item.objects.all()
    serializer_class = serializers.Questionnaire_Item
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Questionnaire_Item
    ordering_fields = "__all__"


class Questionnaire_EnableWhen(viewsets.ModelViewSet):
    queryset = models.Questionnaire_EnableWhen.objects.all()
    serializer_class = serializers.Questionnaire_EnableWhen
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Questionnaire_EnableWhen
    ordering_fields = "__all__"
    search_fields = [
        "$answerDate",
        "$answerDateTime",
        "$answerTime",
        "$answerString",
    ]


class Questionnaire_AnswerOption(viewsets.ModelViewSet):
    queryset = models.Questionnaire_AnswerOption.objects.all()
    serializer_class = serializers.Questionnaire_AnswerOption
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Questionnaire_AnswerOption
    ordering_fields = "__all__"
    search_fields = [
        "$valueDate",
        "$valueTime",
        "$valueString",
    ]


class Questionnaire_Initial(viewsets.ModelViewSet):
    queryset = models.Questionnaire_Initial.objects.all()
    serializer_class = serializers.Questionnaire_Initial
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Questionnaire_Initial
    ordering_fields = "__all__"
    search_fields = [
        "$valueDate",
        "$valueDateTime",
        "$valueTime",
        "$valueString",
        "$valueUri",
    ]


class QuestionnaireResponse(viewsets.ModelViewSet):
    queryset = models.QuestionnaireResponse.objects.all()
    serializer_class = serializers.QuestionnaireResponse
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.QuestionnaireResponse
    ordering_fields = "__all__"


class QuestionnaireResponse_Item(viewsets.ModelViewSet):
    queryset = models.QuestionnaireResponse_Item.objects.all()
    serializer_class = serializers.QuestionnaireResponse_Item
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.QuestionnaireResponse_Item
    ordering_fields = "__all__"


class QuestionnaireResponse_Answer(viewsets.ModelViewSet):
    queryset = models.QuestionnaireResponse_Answer.objects.all()
    serializer_class = serializers.QuestionnaireResponse_Answer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.QuestionnaireResponse_Answer
    ordering_fields = "__all__"
    search_fields = [
        "$valueDate",
        "$valueDateTime",
        "$valueTime",
        "$valueString",
        "$valueUri",
    ]


class RelatedPerson(viewsets.ModelViewSet):
    queryset = models.RelatedPerson.objects.all()
    serializer_class = serializers.RelatedPerson
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.RelatedPerson
    ordering_fields = "__all__"


class RelatedPerson_Communication(viewsets.ModelViewSet):
    queryset = models.RelatedPerson_Communication.objects.all()
    serializer_class = serializers.RelatedPerson_Communication
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.RelatedPerson_Communication
    ordering_fields = "__all__"


class RequestGroup(viewsets.ModelViewSet):
    queryset = models.RequestGroup.objects.all()
    serializer_class = serializers.RequestGroup
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.RequestGroup
    ordering_fields = "__all__"


class RequestGroup_Action(viewsets.ModelViewSet):
    queryset = models.RequestGroup_Action.objects.all()
    serializer_class = serializers.RequestGroup_Action
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.RequestGroup_Action
    ordering_fields = "__all__"
    search_fields = [
        "$timingDateTime",
    ]


class RequestGroup_Condition(viewsets.ModelViewSet):
    queryset = models.RequestGroup_Condition.objects.all()
    serializer_class = serializers.RequestGroup_Condition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.RequestGroup_Condition
    ordering_fields = "__all__"


class RequestGroup_RelatedAction(viewsets.ModelViewSet):
    queryset = models.RequestGroup_RelatedAction.objects.all()
    serializer_class = serializers.RequestGroup_RelatedAction
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.RequestGroup_RelatedAction
    ordering_fields = "__all__"


class ResearchDefinition(viewsets.ModelViewSet):
    queryset = models.ResearchDefinition.objects.all()
    serializer_class = serializers.ResearchDefinition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ResearchDefinition
    ordering_fields = "__all__"


class ResearchElementDefinition(viewsets.ModelViewSet):
    queryset = models.ResearchElementDefinition.objects.all()
    serializer_class = serializers.ResearchElementDefinition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ResearchElementDefinition
    ordering_fields = "__all__"


class ResearchElementDefinition_Characteristic(viewsets.ModelViewSet):
    queryset = models.ResearchElementDefinition_Characteristic.objects.all()
    serializer_class = serializers.ResearchElementDefinition_Characteristic
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ResearchElementDefinition_Characteristic
    ordering_fields = "__all__"
    search_fields = [
        "$definitionCanonical",
        "$studyEffectiveDateTime",
        "$participantEffectiveDateTime",
    ]


class ResearchStudy(viewsets.ModelViewSet):
    queryset = models.ResearchStudy.objects.all()
    serializer_class = serializers.ResearchStudy
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ResearchStudy
    ordering_fields = "__all__"


class ResearchStudy_Arm(viewsets.ModelViewSet):
    queryset = models.ResearchStudy_Arm.objects.all()
    serializer_class = serializers.ResearchStudy_Arm
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ResearchStudy_Arm
    ordering_fields = "__all__"


class ResearchStudy_Objective(viewsets.ModelViewSet):
    queryset = models.ResearchStudy_Objective.objects.all()
    serializer_class = serializers.ResearchStudy_Objective
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ResearchStudy_Objective
    ordering_fields = "__all__"


class ResearchSubject(viewsets.ModelViewSet):
    queryset = models.ResearchSubject.objects.all()
    serializer_class = serializers.ResearchSubject
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ResearchSubject
    ordering_fields = "__all__"


class RiskAssessment(viewsets.ModelViewSet):
    queryset = models.RiskAssessment.objects.all()
    serializer_class = serializers.RiskAssessment
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.RiskAssessment
    ordering_fields = "__all__"
    search_fields = [
        "$occurrenceDateTime",
    ]


class RiskAssessment_Prediction(viewsets.ModelViewSet):
    queryset = models.RiskAssessment_Prediction.objects.all()
    serializer_class = serializers.RiskAssessment_Prediction
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.RiskAssessment_Prediction
    ordering_fields = "__all__"


class RiskEvidenceSynthesis(viewsets.ModelViewSet):
    queryset = models.RiskEvidenceSynthesis.objects.all()
    serializer_class = serializers.RiskEvidenceSynthesis
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.RiskEvidenceSynthesis
    ordering_fields = "__all__"


class RiskEvidenceSynthesis_SampleSize(viewsets.ModelViewSet):
    queryset = models.RiskEvidenceSynthesis_SampleSize.objects.all()
    serializer_class = serializers.RiskEvidenceSynthesis_SampleSize
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.RiskEvidenceSynthesis_SampleSize
    ordering_fields = "__all__"


class RiskEvidenceSynthesis_RiskEstimate(viewsets.ModelViewSet):
    queryset = models.RiskEvidenceSynthesis_RiskEstimate.objects.all()
    serializer_class = serializers.RiskEvidenceSynthesis_RiskEstimate
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.RiskEvidenceSynthesis_RiskEstimate
    ordering_fields = "__all__"


class RiskEvidenceSynthesis_PrecisionEstimate(viewsets.ModelViewSet):
    queryset = models.RiskEvidenceSynthesis_PrecisionEstimate.objects.all()
    serializer_class = serializers.RiskEvidenceSynthesis_PrecisionEstimate
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.RiskEvidenceSynthesis_PrecisionEstimate
    ordering_fields = "__all__"


class RiskEvidenceSynthesis_Certainty(viewsets.ModelViewSet):
    queryset = models.RiskEvidenceSynthesis_Certainty.objects.all()
    serializer_class = serializers.RiskEvidenceSynthesis_Certainty
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.RiskEvidenceSynthesis_Certainty
    ordering_fields = "__all__"


class RiskEvidenceSynthesis_CertaintySubcomponent(viewsets.ModelViewSet):
    queryset = models.RiskEvidenceSynthesis_CertaintySubcomponent.objects.all()
    serializer_class = serializers.RiskEvidenceSynthesis_CertaintySubcomponent
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.RiskEvidenceSynthesis_CertaintySubcomponent
    ordering_fields = "__all__"


class Schedule(viewsets.ModelViewSet):
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.Schedule
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Schedule
    ordering_fields = "__all__"


class SearchParameter(viewsets.ModelViewSet):
    queryset = models.SearchParameter.objects.all()
    serializer_class = serializers.SearchParameter
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SearchParameter
    ordering_fields = "__all__"


class SearchParameter_Component(viewsets.ModelViewSet):
    queryset = models.SearchParameter_Component.objects.all()
    serializer_class = serializers.SearchParameter_Component
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SearchParameter_Component
    ordering_fields = "__all__"


class ServiceRequest(viewsets.ModelViewSet):
    queryset = models.ServiceRequest.objects.all()
    serializer_class = serializers.ServiceRequest
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ServiceRequest
    ordering_fields = "__all__"
    search_fields = [
        "$occurrenceDateTime",
    ]


class Slot(viewsets.ModelViewSet):
    queryset = models.Slot.objects.all()
    serializer_class = serializers.Slot
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Slot
    ordering_fields = "__all__"


class Specimen(viewsets.ModelViewSet):
    queryset = models.Specimen.objects.all()
    serializer_class = serializers.Specimen
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Specimen
    ordering_fields = "__all__"


class Specimen_Collection(viewsets.ModelViewSet):
    queryset = models.Specimen_Collection.objects.all()
    serializer_class = serializers.Specimen_Collection
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Specimen_Collection
    ordering_fields = "__all__"
    search_fields = [
        "$collectedDateTime",
    ]


class Specimen_Processing(viewsets.ModelViewSet):
    queryset = models.Specimen_Processing.objects.all()
    serializer_class = serializers.Specimen_Processing
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Specimen_Processing
    ordering_fields = "__all__"
    search_fields = [
        "$timeDateTime",
    ]


class Specimen_Container(viewsets.ModelViewSet):
    queryset = models.Specimen_Container.objects.all()
    serializer_class = serializers.Specimen_Container
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Specimen_Container
    ordering_fields = "__all__"


class SpecimenDefinition(viewsets.ModelViewSet):
    queryset = models.SpecimenDefinition.objects.all()
    serializer_class = serializers.SpecimenDefinition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SpecimenDefinition
    ordering_fields = "__all__"


class SpecimenDefinition_TypeTested(viewsets.ModelViewSet):
    queryset = models.SpecimenDefinition_TypeTested.objects.all()
    serializer_class = serializers.SpecimenDefinition_TypeTested
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SpecimenDefinition_TypeTested
    ordering_fields = "__all__"


class SpecimenDefinition_Container(viewsets.ModelViewSet):
    queryset = models.SpecimenDefinition_Container.objects.all()
    serializer_class = serializers.SpecimenDefinition_Container
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SpecimenDefinition_Container
    ordering_fields = "__all__"
    search_fields = [
        "$minimumVolumeString",
    ]


class SpecimenDefinition_Additive(viewsets.ModelViewSet):
    queryset = models.SpecimenDefinition_Additive.objects.all()
    serializer_class = serializers.SpecimenDefinition_Additive
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SpecimenDefinition_Additive
    ordering_fields = "__all__"


class SpecimenDefinition_Handling(viewsets.ModelViewSet):
    queryset = models.SpecimenDefinition_Handling.objects.all()
    serializer_class = serializers.SpecimenDefinition_Handling
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SpecimenDefinition_Handling
    ordering_fields = "__all__"


class StructureDefinition(viewsets.ModelViewSet):
    queryset = models.StructureDefinition.objects.all()
    serializer_class = serializers.StructureDefinition
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.StructureDefinition
    ordering_fields = "__all__"


class StructureDefinition_Mapping(viewsets.ModelViewSet):
    queryset = models.StructureDefinition_Mapping.objects.all()
    serializer_class = serializers.StructureDefinition_Mapping
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.StructureDefinition_Mapping
    ordering_fields = "__all__"


class StructureDefinition_Context(viewsets.ModelViewSet):
    queryset = models.StructureDefinition_Context.objects.all()
    serializer_class = serializers.StructureDefinition_Context
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.StructureDefinition_Context
    ordering_fields = "__all__"


class StructureDefinition_Snapshot(viewsets.ModelViewSet):
    queryset = models.StructureDefinition_Snapshot.objects.all()
    serializer_class = serializers.StructureDefinition_Snapshot
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.StructureDefinition_Snapshot
    ordering_fields = "__all__"


class StructureDefinition_Differential(viewsets.ModelViewSet):
    queryset = models.StructureDefinition_Differential.objects.all()
    serializer_class = serializers.StructureDefinition_Differential
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.StructureDefinition_Differential
    ordering_fields = "__all__"


class StructureMap(viewsets.ModelViewSet):
    queryset = models.StructureMap.objects.all()
    serializer_class = serializers.StructureMap
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.StructureMap
    ordering_fields = "__all__"


class StructureMap_Structure(viewsets.ModelViewSet):
    queryset = models.StructureMap_Structure.objects.all()
    serializer_class = serializers.StructureMap_Structure
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.StructureMap_Structure
    ordering_fields = "__all__"


class StructureMap_Group(viewsets.ModelViewSet):
    queryset = models.StructureMap_Group.objects.all()
    serializer_class = serializers.StructureMap_Group
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.StructureMap_Group
    ordering_fields = "__all__"


class StructureMap_Input(viewsets.ModelViewSet):
    queryset = models.StructureMap_Input.objects.all()
    serializer_class = serializers.StructureMap_Input
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.StructureMap_Input
    ordering_fields = "__all__"


class StructureMap_Rule(viewsets.ModelViewSet):
    queryset = models.StructureMap_Rule.objects.all()
    serializer_class = serializers.StructureMap_Rule
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.StructureMap_Rule
    ordering_fields = "__all__"


class StructureMap_Source(viewsets.ModelViewSet):
    queryset = models.StructureMap_Source.objects.all()
    serializer_class = serializers.StructureMap_Source
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.StructureMap_Source
    ordering_fields = "__all__"
    search_fields = [
        "$defaultValueBase64Binary",
        "$defaultValueCanonical",
        "$defaultValueCode",
        "$defaultValueDate",
        "$defaultValueDateTime",
        "$defaultValueId",
        "$defaultValueInstant",
        "$defaultValueMarkdown",
        "$defaultValueOid",
        "$defaultValueString",
        "$defaultValueTime",
        "$defaultValueUri",
        "$defaultValueUrl",
        "$defaultValueUuid",
    ]


class StructureMap_Target(viewsets.ModelViewSet):
    queryset = models.StructureMap_Target.objects.all()
    serializer_class = serializers.StructureMap_Target
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.StructureMap_Target
    ordering_fields = "__all__"


class StructureMap_Parameter(viewsets.ModelViewSet):
    queryset = models.StructureMap_Parameter.objects.all()
    serializer_class = serializers.StructureMap_Parameter
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.StructureMap_Parameter
    ordering_fields = "__all__"
    search_fields = [
        "$valueId",
        "$valueString",
    ]


class StructureMap_Dependent(viewsets.ModelViewSet):
    queryset = models.StructureMap_Dependent.objects.all()
    serializer_class = serializers.StructureMap_Dependent
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.StructureMap_Dependent
    ordering_fields = "__all__"


class Subscription(viewsets.ModelViewSet):
    queryset = models.Subscription.objects.all()
    serializer_class = serializers.Subscription
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Subscription
    ordering_fields = "__all__"


class Subscription_Channel(viewsets.ModelViewSet):
    queryset = models.Subscription_Channel.objects.all()
    serializer_class = serializers.Subscription_Channel
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Subscription_Channel
    ordering_fields = "__all__"


class Substance(viewsets.ModelViewSet):
    queryset = models.Substance.objects.all()
    serializer_class = serializers.Substance
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Substance
    ordering_fields = "__all__"


class Substance_Instance(viewsets.ModelViewSet):
    queryset = models.Substance_Instance.objects.all()
    serializer_class = serializers.Substance_Instance
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Substance_Instance
    ordering_fields = "__all__"


class Substance_Ingredient(viewsets.ModelViewSet):
    queryset = models.Substance_Ingredient.objects.all()
    serializer_class = serializers.Substance_Ingredient
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Substance_Ingredient
    ordering_fields = "__all__"


class SubstanceNucleicAcid(viewsets.ModelViewSet):
    queryset = models.SubstanceNucleicAcid.objects.all()
    serializer_class = serializers.SubstanceNucleicAcid
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceNucleicAcid
    ordering_fields = "__all__"


class SubstanceNucleicAcid_Subunit(viewsets.ModelViewSet):
    queryset = models.SubstanceNucleicAcid_Subunit.objects.all()
    serializer_class = serializers.SubstanceNucleicAcid_Subunit
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceNucleicAcid_Subunit
    ordering_fields = "__all__"


class SubstanceNucleicAcid_Linkage(viewsets.ModelViewSet):
    queryset = models.SubstanceNucleicAcid_Linkage.objects.all()
    serializer_class = serializers.SubstanceNucleicAcid_Linkage
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceNucleicAcid_Linkage
    ordering_fields = "__all__"


class SubstanceNucleicAcid_Sugar(viewsets.ModelViewSet):
    queryset = models.SubstanceNucleicAcid_Sugar.objects.all()
    serializer_class = serializers.SubstanceNucleicAcid_Sugar
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceNucleicAcid_Sugar
    ordering_fields = "__all__"


class SubstancePolymer(viewsets.ModelViewSet):
    queryset = models.SubstancePolymer.objects.all()
    serializer_class = serializers.SubstancePolymer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstancePolymer
    ordering_fields = "__all__"


class SubstancePolymer_MonomerSet(viewsets.ModelViewSet):
    queryset = models.SubstancePolymer_MonomerSet.objects.all()
    serializer_class = serializers.SubstancePolymer_MonomerSet
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstancePolymer_MonomerSet
    ordering_fields = "__all__"


class SubstancePolymer_StartingMaterial(viewsets.ModelViewSet):
    queryset = models.SubstancePolymer_StartingMaterial.objects.all()
    serializer_class = serializers.SubstancePolymer_StartingMaterial
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstancePolymer_StartingMaterial
    ordering_fields = "__all__"


class SubstancePolymer_Repeat(viewsets.ModelViewSet):
    queryset = models.SubstancePolymer_Repeat.objects.all()
    serializer_class = serializers.SubstancePolymer_Repeat
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstancePolymer_Repeat
    ordering_fields = "__all__"


class SubstancePolymer_RepeatUnit(viewsets.ModelViewSet):
    queryset = models.SubstancePolymer_RepeatUnit.objects.all()
    serializer_class = serializers.SubstancePolymer_RepeatUnit
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstancePolymer_RepeatUnit
    ordering_fields = "__all__"


class SubstancePolymer_DegreeOfPolymerisation(viewsets.ModelViewSet):
    queryset = models.SubstancePolymer_DegreeOfPolymerisation.objects.all()
    serializer_class = serializers.SubstancePolymer_DegreeOfPolymerisation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstancePolymer_DegreeOfPolymerisation
    ordering_fields = "__all__"


class SubstancePolymer_StructuralRepresentation(viewsets.ModelViewSet):
    queryset = models.SubstancePolymer_StructuralRepresentation.objects.all()
    serializer_class = serializers.SubstancePolymer_StructuralRepresentation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstancePolymer_StructuralRepresentation
    ordering_fields = "__all__"


class SubstanceProtein(viewsets.ModelViewSet):
    queryset = models.SubstanceProtein.objects.all()
    serializer_class = serializers.SubstanceProtein
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceProtein
    ordering_fields = "__all__"


class SubstanceProtein_Subunit(viewsets.ModelViewSet):
    queryset = models.SubstanceProtein_Subunit.objects.all()
    serializer_class = serializers.SubstanceProtein_Subunit
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceProtein_Subunit
    ordering_fields = "__all__"


class SubstanceReferenceInformation(viewsets.ModelViewSet):
    queryset = models.SubstanceReferenceInformation.objects.all()
    serializer_class = serializers.SubstanceReferenceInformation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceReferenceInformation
    ordering_fields = "__all__"


class SubstanceReferenceInformation_Gene(viewsets.ModelViewSet):
    queryset = models.SubstanceReferenceInformation_Gene.objects.all()
    serializer_class = serializers.SubstanceReferenceInformation_Gene
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceReferenceInformation_Gene
    ordering_fields = "__all__"


class SubstanceReferenceInformation_GeneElement(viewsets.ModelViewSet):
    queryset = models.SubstanceReferenceInformation_GeneElement.objects.all()
    serializer_class = serializers.SubstanceReferenceInformation_GeneElement
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceReferenceInformation_GeneElement
    ordering_fields = "__all__"


class SubstanceReferenceInformation_Classification(viewsets.ModelViewSet):
    queryset = models.SubstanceReferenceInformation_Classification.objects.all()
    serializer_class = serializers.SubstanceReferenceInformation_Classification
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceReferenceInformation_Classification
    ordering_fields = "__all__"


class SubstanceReferenceInformation_Target(viewsets.ModelViewSet):
    queryset = models.SubstanceReferenceInformation_Target.objects.all()
    serializer_class = serializers.SubstanceReferenceInformation_Target
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceReferenceInformation_Target
    ordering_fields = "__all__"
    search_fields = [
        "$amountString",
    ]


class SubstanceSourceMaterial(viewsets.ModelViewSet):
    queryset = models.SubstanceSourceMaterial.objects.all()
    serializer_class = serializers.SubstanceSourceMaterial
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceSourceMaterial
    ordering_fields = "__all__"


class SubstanceSourceMaterial_FractionDescription(viewsets.ModelViewSet):
    queryset = models.SubstanceSourceMaterial_FractionDescription.objects.all()
    serializer_class = serializers.SubstanceSourceMaterial_FractionDescription
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceSourceMaterial_FractionDescription
    ordering_fields = "__all__"


class SubstanceSourceMaterial_Organism(viewsets.ModelViewSet):
    queryset = models.SubstanceSourceMaterial_Organism.objects.all()
    serializer_class = serializers.SubstanceSourceMaterial_Organism
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceSourceMaterial_Organism
    ordering_fields = "__all__"


class SubstanceSourceMaterial_Author(viewsets.ModelViewSet):
    queryset = models.SubstanceSourceMaterial_Author.objects.all()
    serializer_class = serializers.SubstanceSourceMaterial_Author
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceSourceMaterial_Author
    ordering_fields = "__all__"


class SubstanceSourceMaterial_Hybrid(viewsets.ModelViewSet):
    queryset = models.SubstanceSourceMaterial_Hybrid.objects.all()
    serializer_class = serializers.SubstanceSourceMaterial_Hybrid
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceSourceMaterial_Hybrid
    ordering_fields = "__all__"


class SubstanceSourceMaterial_OrganismGeneral(viewsets.ModelViewSet):
    queryset = models.SubstanceSourceMaterial_OrganismGeneral.objects.all()
    serializer_class = serializers.SubstanceSourceMaterial_OrganismGeneral
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceSourceMaterial_OrganismGeneral
    ordering_fields = "__all__"


class SubstanceSourceMaterial_PartDescription(viewsets.ModelViewSet):
    queryset = models.SubstanceSourceMaterial_PartDescription.objects.all()
    serializer_class = serializers.SubstanceSourceMaterial_PartDescription
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceSourceMaterial_PartDescription
    ordering_fields = "__all__"


class SubstanceSpecification(viewsets.ModelViewSet):
    queryset = models.SubstanceSpecification.objects.all()
    serializer_class = serializers.SubstanceSpecification
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceSpecification
    ordering_fields = "__all__"


class SubstanceSpecification_Moiety(viewsets.ModelViewSet):
    queryset = models.SubstanceSpecification_Moiety.objects.all()
    serializer_class = serializers.SubstanceSpecification_Moiety
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceSpecification_Moiety
    ordering_fields = "__all__"
    search_fields = [
        "$amountString",
    ]


class SubstanceSpecification_Property(viewsets.ModelViewSet):
    queryset = models.SubstanceSpecification_Property.objects.all()
    serializer_class = serializers.SubstanceSpecification_Property
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceSpecification_Property
    ordering_fields = "__all__"
    search_fields = [
        "$amountString",
    ]


class SubstanceSpecification_Structure(viewsets.ModelViewSet):
    queryset = models.SubstanceSpecification_Structure.objects.all()
    serializer_class = serializers.SubstanceSpecification_Structure
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceSpecification_Structure
    ordering_fields = "__all__"


class SubstanceSpecification_Isotope(viewsets.ModelViewSet):
    queryset = models.SubstanceSpecification_Isotope.objects.all()
    serializer_class = serializers.SubstanceSpecification_Isotope
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceSpecification_Isotope
    ordering_fields = "__all__"


class SubstanceSpecification_MolecularWeight(viewsets.ModelViewSet):
    queryset = models.SubstanceSpecification_MolecularWeight.objects.all()
    serializer_class = serializers.SubstanceSpecification_MolecularWeight
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceSpecification_MolecularWeight
    ordering_fields = "__all__"


class SubstanceSpecification_Representation(viewsets.ModelViewSet):
    queryset = models.SubstanceSpecification_Representation.objects.all()
    serializer_class = serializers.SubstanceSpecification_Representation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceSpecification_Representation
    ordering_fields = "__all__"


class SubstanceSpecification_Code(viewsets.ModelViewSet):
    queryset = models.SubstanceSpecification_Code.objects.all()
    serializer_class = serializers.SubstanceSpecification_Code
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceSpecification_Code
    ordering_fields = "__all__"


class SubstanceSpecification_Name(viewsets.ModelViewSet):
    queryset = models.SubstanceSpecification_Name.objects.all()
    serializer_class = serializers.SubstanceSpecification_Name
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceSpecification_Name
    ordering_fields = "__all__"


class SubstanceSpecification_Official(viewsets.ModelViewSet):
    queryset = models.SubstanceSpecification_Official.objects.all()
    serializer_class = serializers.SubstanceSpecification_Official
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceSpecification_Official
    ordering_fields = "__all__"


class SubstanceSpecification_Relationship(viewsets.ModelViewSet):
    queryset = models.SubstanceSpecification_Relationship.objects.all()
    serializer_class = serializers.SubstanceSpecification_Relationship
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SubstanceSpecification_Relationship
    ordering_fields = "__all__"
    search_fields = [
        "$amountString",
    ]


class SupplyDelivery(viewsets.ModelViewSet):
    queryset = models.SupplyDelivery.objects.all()
    serializer_class = serializers.SupplyDelivery
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SupplyDelivery
    ordering_fields = "__all__"
    search_fields = [
        "$occurrenceDateTime",
    ]


class SupplyDelivery_SuppliedItem(viewsets.ModelViewSet):
    queryset = models.SupplyDelivery_SuppliedItem.objects.all()
    serializer_class = serializers.SupplyDelivery_SuppliedItem
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SupplyDelivery_SuppliedItem
    ordering_fields = "__all__"


class SupplyRequest(viewsets.ModelViewSet):
    queryset = models.SupplyRequest.objects.all()
    serializer_class = serializers.SupplyRequest
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SupplyRequest
    ordering_fields = "__all__"
    search_fields = [
        "$occurrenceDateTime",
    ]


class SupplyRequest_Parameter(viewsets.ModelViewSet):
    queryset = models.SupplyRequest_Parameter.objects.all()
    serializer_class = serializers.SupplyRequest_Parameter
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.SupplyRequest_Parameter
    ordering_fields = "__all__"


class Task(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.Task
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Task
    ordering_fields = "__all__"


class Task_Restriction(viewsets.ModelViewSet):
    queryset = models.Task_Restriction.objects.all()
    serializer_class = serializers.Task_Restriction
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Task_Restriction
    ordering_fields = "__all__"


class Task_Input(viewsets.ModelViewSet):
    queryset = models.Task_Input.objects.all()
    serializer_class = serializers.Task_Input
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Task_Input
    ordering_fields = "__all__"
    search_fields = [
        "$valueBase64Binary",
        "$valueCanonical",
        "$valueCode",
        "$valueDate",
        "$valueDateTime",
        "$valueId",
        "$valueInstant",
        "$valueMarkdown",
        "$valueOid",
        "$valueString",
        "$valueTime",
        "$valueUri",
        "$valueUrl",
        "$valueUuid",
    ]


class Task_Output(viewsets.ModelViewSet):
    queryset = models.Task_Output.objects.all()
    serializer_class = serializers.Task_Output
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.Task_Output
    ordering_fields = "__all__"
    search_fields = [
        "$valueBase64Binary",
        "$valueCanonical",
        "$valueCode",
        "$valueDate",
        "$valueDateTime",
        "$valueId",
        "$valueInstant",
        "$valueMarkdown",
        "$valueOid",
        "$valueString",
        "$valueTime",
        "$valueUri",
        "$valueUrl",
        "$valueUuid",
    ]


class TerminologyCapabilities(viewsets.ModelViewSet):
    queryset = models.TerminologyCapabilities.objects.all()
    serializer_class = serializers.TerminologyCapabilities
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TerminologyCapabilities
    ordering_fields = "__all__"


class TerminologyCapabilities_Software(viewsets.ModelViewSet):
    queryset = models.TerminologyCapabilities_Software.objects.all()
    serializer_class = serializers.TerminologyCapabilities_Software
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TerminologyCapabilities_Software
    ordering_fields = "__all__"


class TerminologyCapabilities_Implementation(viewsets.ModelViewSet):
    queryset = models.TerminologyCapabilities_Implementation.objects.all()
    serializer_class = serializers.TerminologyCapabilities_Implementation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TerminologyCapabilities_Implementation
    ordering_fields = "__all__"


class TerminologyCapabilities_CodeSystem(viewsets.ModelViewSet):
    queryset = models.TerminologyCapabilities_CodeSystem.objects.all()
    serializer_class = serializers.TerminologyCapabilities_CodeSystem
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TerminologyCapabilities_CodeSystem
    ordering_fields = "__all__"


class TerminologyCapabilities_Version(viewsets.ModelViewSet):
    queryset = models.TerminologyCapabilities_Version.objects.all()
    serializer_class = serializers.TerminologyCapabilities_Version
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TerminologyCapabilities_Version
    ordering_fields = "__all__"


class TerminologyCapabilities_Filter(viewsets.ModelViewSet):
    queryset = models.TerminologyCapabilities_Filter.objects.all()
    serializer_class = serializers.TerminologyCapabilities_Filter
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TerminologyCapabilities_Filter
    ordering_fields = "__all__"


class TerminologyCapabilities_Expansion(viewsets.ModelViewSet):
    queryset = models.TerminologyCapabilities_Expansion.objects.all()
    serializer_class = serializers.TerminologyCapabilities_Expansion
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TerminologyCapabilities_Expansion
    ordering_fields = "__all__"


class TerminologyCapabilities_Parameter(viewsets.ModelViewSet):
    queryset = models.TerminologyCapabilities_Parameter.objects.all()
    serializer_class = serializers.TerminologyCapabilities_Parameter
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TerminologyCapabilities_Parameter
    ordering_fields = "__all__"


class TerminologyCapabilities_ValidateCode(viewsets.ModelViewSet):
    queryset = models.TerminologyCapabilities_ValidateCode.objects.all()
    serializer_class = serializers.TerminologyCapabilities_ValidateCode
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TerminologyCapabilities_ValidateCode
    ordering_fields = "__all__"


class TerminologyCapabilities_Translation(viewsets.ModelViewSet):
    queryset = models.TerminologyCapabilities_Translation.objects.all()
    serializer_class = serializers.TerminologyCapabilities_Translation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TerminologyCapabilities_Translation
    ordering_fields = "__all__"


class TerminologyCapabilities_Closure(viewsets.ModelViewSet):
    queryset = models.TerminologyCapabilities_Closure.objects.all()
    serializer_class = serializers.TerminologyCapabilities_Closure
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TerminologyCapabilities_Closure
    ordering_fields = "__all__"


class TestReport(viewsets.ModelViewSet):
    queryset = models.TestReport.objects.all()
    serializer_class = serializers.TestReport
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestReport
    ordering_fields = "__all__"


class TestReport_Participant(viewsets.ModelViewSet):
    queryset = models.TestReport_Participant.objects.all()
    serializer_class = serializers.TestReport_Participant
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestReport_Participant
    ordering_fields = "__all__"


class TestReport_Setup(viewsets.ModelViewSet):
    queryset = models.TestReport_Setup.objects.all()
    serializer_class = serializers.TestReport_Setup
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestReport_Setup
    ordering_fields = "__all__"


class TestReport_Action(viewsets.ModelViewSet):
    queryset = models.TestReport_Action.objects.all()
    serializer_class = serializers.TestReport_Action
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestReport_Action
    ordering_fields = "__all__"


class TestReport_Operation(viewsets.ModelViewSet):
    queryset = models.TestReport_Operation.objects.all()
    serializer_class = serializers.TestReport_Operation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestReport_Operation
    ordering_fields = "__all__"


class TestReport_Assert(viewsets.ModelViewSet):
    queryset = models.TestReport_Assert.objects.all()
    serializer_class = serializers.TestReport_Assert
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestReport_Assert
    ordering_fields = "__all__"


class TestReport_Test(viewsets.ModelViewSet):
    queryset = models.TestReport_Test.objects.all()
    serializer_class = serializers.TestReport_Test
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestReport_Test
    ordering_fields = "__all__"


class TestReport_Action1(viewsets.ModelViewSet):
    queryset = models.TestReport_Action1.objects.all()
    serializer_class = serializers.TestReport_Action1
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestReport_Action1
    ordering_fields = "__all__"


class TestReport_Teardown(viewsets.ModelViewSet):
    queryset = models.TestReport_Teardown.objects.all()
    serializer_class = serializers.TestReport_Teardown
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestReport_Teardown
    ordering_fields = "__all__"


class TestReport_Action2(viewsets.ModelViewSet):
    queryset = models.TestReport_Action2.objects.all()
    serializer_class = serializers.TestReport_Action2
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestReport_Action2
    ordering_fields = "__all__"


class TestScript(viewsets.ModelViewSet):
    queryset = models.TestScript.objects.all()
    serializer_class = serializers.TestScript
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestScript
    ordering_fields = "__all__"


class TestScript_Origin(viewsets.ModelViewSet):
    queryset = models.TestScript_Origin.objects.all()
    serializer_class = serializers.TestScript_Origin
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestScript_Origin
    ordering_fields = "__all__"


class TestScript_Destination(viewsets.ModelViewSet):
    queryset = models.TestScript_Destination.objects.all()
    serializer_class = serializers.TestScript_Destination
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestScript_Destination
    ordering_fields = "__all__"


class TestScript_Metadata(viewsets.ModelViewSet):
    queryset = models.TestScript_Metadata.objects.all()
    serializer_class = serializers.TestScript_Metadata
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestScript_Metadata
    ordering_fields = "__all__"


class TestScript_Link(viewsets.ModelViewSet):
    queryset = models.TestScript_Link.objects.all()
    serializer_class = serializers.TestScript_Link
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestScript_Link
    ordering_fields = "__all__"


class TestScript_Capability(viewsets.ModelViewSet):
    queryset = models.TestScript_Capability.objects.all()
    serializer_class = serializers.TestScript_Capability
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestScript_Capability
    ordering_fields = "__all__"


class TestScript_Fixture(viewsets.ModelViewSet):
    queryset = models.TestScript_Fixture.objects.all()
    serializer_class = serializers.TestScript_Fixture
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestScript_Fixture
    ordering_fields = "__all__"


class TestScript_Variable(viewsets.ModelViewSet):
    queryset = models.TestScript_Variable.objects.all()
    serializer_class = serializers.TestScript_Variable
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestScript_Variable
    ordering_fields = "__all__"


class TestScript_Setup(viewsets.ModelViewSet):
    queryset = models.TestScript_Setup.objects.all()
    serializer_class = serializers.TestScript_Setup
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestScript_Setup
    ordering_fields = "__all__"


class TestScript_Action(viewsets.ModelViewSet):
    queryset = models.TestScript_Action.objects.all()
    serializer_class = serializers.TestScript_Action
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestScript_Action
    ordering_fields = "__all__"


class TestScript_Operation(viewsets.ModelViewSet):
    queryset = models.TestScript_Operation.objects.all()
    serializer_class = serializers.TestScript_Operation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestScript_Operation
    ordering_fields = "__all__"


class TestScript_RequestHeader(viewsets.ModelViewSet):
    queryset = models.TestScript_RequestHeader.objects.all()
    serializer_class = serializers.TestScript_RequestHeader
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestScript_RequestHeader
    ordering_fields = "__all__"


class TestScript_Assert(viewsets.ModelViewSet):
    queryset = models.TestScript_Assert.objects.all()
    serializer_class = serializers.TestScript_Assert
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestScript_Assert
    ordering_fields = "__all__"


class TestScript_Test(viewsets.ModelViewSet):
    queryset = models.TestScript_Test.objects.all()
    serializer_class = serializers.TestScript_Test
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestScript_Test
    ordering_fields = "__all__"


class TestScript_Action1(viewsets.ModelViewSet):
    queryset = models.TestScript_Action1.objects.all()
    serializer_class = serializers.TestScript_Action1
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestScript_Action1
    ordering_fields = "__all__"


class TestScript_Teardown(viewsets.ModelViewSet):
    queryset = models.TestScript_Teardown.objects.all()
    serializer_class = serializers.TestScript_Teardown
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestScript_Teardown
    ordering_fields = "__all__"


class TestScript_Action2(viewsets.ModelViewSet):
    queryset = models.TestScript_Action2.objects.all()
    serializer_class = serializers.TestScript_Action2
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.TestScript_Action2
    ordering_fields = "__all__"


class ValueSet(viewsets.ModelViewSet):
    queryset = models.ValueSet.objects.all()
    serializer_class = serializers.ValueSet
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ValueSet
    ordering_fields = "__all__"


class ValueSet_Compose(viewsets.ModelViewSet):
    queryset = models.ValueSet_Compose.objects.all()
    serializer_class = serializers.ValueSet_Compose
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ValueSet_Compose
    ordering_fields = "__all__"


class ValueSet_Include(viewsets.ModelViewSet):
    queryset = models.ValueSet_Include.objects.all()
    serializer_class = serializers.ValueSet_Include
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ValueSet_Include
    ordering_fields = "__all__"


class ValueSet_Concept(viewsets.ModelViewSet):
    queryset = models.ValueSet_Concept.objects.all()
    serializer_class = serializers.ValueSet_Concept
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ValueSet_Concept
    ordering_fields = "__all__"


class ValueSet_Designation(viewsets.ModelViewSet):
    queryset = models.ValueSet_Designation.objects.all()
    serializer_class = serializers.ValueSet_Designation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ValueSet_Designation
    ordering_fields = "__all__"


class ValueSet_Filter(viewsets.ModelViewSet):
    queryset = models.ValueSet_Filter.objects.all()
    serializer_class = serializers.ValueSet_Filter
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ValueSet_Filter
    ordering_fields = "__all__"


class ValueSet_Expansion(viewsets.ModelViewSet):
    queryset = models.ValueSet_Expansion.objects.all()
    serializer_class = serializers.ValueSet_Expansion
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ValueSet_Expansion
    ordering_fields = "__all__"


class ValueSet_Parameter(viewsets.ModelViewSet):
    queryset = models.ValueSet_Parameter.objects.all()
    serializer_class = serializers.ValueSet_Parameter
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ValueSet_Parameter
    ordering_fields = "__all__"
    search_fields = [
        "$valueString",
        "$valueUri",
        "$valueCode",
        "$valueDateTime",
    ]


class ValueSet_Contains(viewsets.ModelViewSet):
    queryset = models.ValueSet_Contains.objects.all()
    serializer_class = serializers.ValueSet_Contains
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.ValueSet_Contains
    ordering_fields = "__all__"


class VerificationResult(viewsets.ModelViewSet):
    queryset = models.VerificationResult.objects.all()
    serializer_class = serializers.VerificationResult
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.VerificationResult
    ordering_fields = "__all__"


class VerificationResult_PrimarySource(viewsets.ModelViewSet):
    queryset = models.VerificationResult_PrimarySource.objects.all()
    serializer_class = serializers.VerificationResult_PrimarySource
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.VerificationResult_PrimarySource
    ordering_fields = "__all__"


class VerificationResult_Attestation(viewsets.ModelViewSet):
    queryset = models.VerificationResult_Attestation.objects.all()
    serializer_class = serializers.VerificationResult_Attestation
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.VerificationResult_Attestation
    ordering_fields = "__all__"


class VerificationResult_Validator(viewsets.ModelViewSet):
    queryset = models.VerificationResult_Validator.objects.all()
    serializer_class = serializers.VerificationResult_Validator
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.VerificationResult_Validator
    ordering_fields = "__all__"


class VisionPrescription(viewsets.ModelViewSet):
    queryset = models.VisionPrescription.objects.all()
    serializer_class = serializers.VisionPrescription
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.VisionPrescription
    ordering_fields = "__all__"


class VisionPrescription_LensSpecification(viewsets.ModelViewSet):
    queryset = models.VisionPrescription_LensSpecification.objects.all()
    serializer_class = serializers.VisionPrescription_LensSpecification
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.VisionPrescription_LensSpecification
    ordering_fields = "__all__"


class VisionPrescription_Prism(viewsets.ModelViewSet):
    queryset = models.VisionPrescription_Prism.objects.all()
    serializer_class = serializers.VisionPrescription_Prism
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.VisionPrescription_Prism
    ordering_fields = "__all__"
