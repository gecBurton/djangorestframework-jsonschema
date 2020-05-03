from django_filters import rest_framework as filters
from . import models


class Element(filters.FilterSet):
    class Meta:
        model = models.Element
        fields = []


class Extension(filters.FilterSet):
    class Meta:
        model = models.Extension
        fields = {
            "valueDecimal": ["exact", "gte", "lte"],
            "valueInteger": ["exact", "gte", "lte"],
            "valuePositiveInt": ["exact", "gte", "lte"],
            "valueUnsignedInt": ["exact", "gte", "lte"],
        }


class Narrative(filters.FilterSet):
    class Meta:
        model = models.Narrative
        fields = {
            "status": ["exact", "in"],
        }


class Annotation(filters.FilterSet):
    class Meta:
        model = models.Annotation
        fields = {
            "time": ["exact", "gte", "lte"],
        }


class Attachment(filters.FilterSet):
    class Meta:
        model = models.Attachment
        fields = {
            "size": ["exact", "gte", "lte"],
            "creation": ["exact", "gte", "lte"],
        }


class Identifier(filters.FilterSet):
    class Meta:
        model = models.Identifier
        fields = {
            "use": ["exact", "in"],
        }


class CodeableConcept(filters.FilterSet):
    class Meta:
        model = models.CodeableConcept
        fields = []


class Coding(filters.FilterSet):
    class Meta:
        model = models.Coding
        fields = []


class Quantity(filters.FilterSet):
    class Meta:
        model = models.Quantity
        fields = {
            "value": ["exact", "gte", "lte"],
            "comparator": ["exact", "in"],
        }


class Duration(filters.FilterSet):
    class Meta:
        model = models.Duration
        fields = {
            "value": ["exact", "gte", "lte"],
            "comparator": ["exact", "in"],
        }


class Distance(filters.FilterSet):
    class Meta:
        model = models.Distance
        fields = {
            "value": ["exact", "gte", "lte"],
            "comparator": ["exact", "in"],
        }


class Count(filters.FilterSet):
    class Meta:
        model = models.Count
        fields = {
            "value": ["exact", "gte", "lte"],
            "comparator": ["exact", "in"],
        }


class Money(filters.FilterSet):
    class Meta:
        model = models.Money
        fields = {
            "value": ["exact", "gte", "lte"],
        }


class Age(filters.FilterSet):
    class Meta:
        model = models.Age
        fields = {
            "value": ["exact", "gte", "lte"],
            "comparator": ["exact", "in"],
        }


class Range(filters.FilterSet):
    class Meta:
        model = models.Range
        fields = []


class Period(filters.FilterSet):
    class Meta:
        model = models.Period
        fields = {
            "start": ["exact", "gte", "lte"],
            "end": ["exact", "gte", "lte"],
        }


class Ratio(filters.FilterSet):
    class Meta:
        model = models.Ratio
        fields = []


class Reference(filters.FilterSet):
    class Meta:
        model = models.Reference
        fields = []


class SampledData(filters.FilterSet):
    class Meta:
        model = models.SampledData
        fields = {
            "period": ["exact", "gte", "lte"],
            "factor": ["exact", "gte", "lte"],
            "lowerLimit": ["exact", "gte", "lte"],
            "upperLimit": ["exact", "gte", "lte"],
            "dimensions": ["exact", "gte", "lte"],
        }


class Signature(filters.FilterSet):
    class Meta:
        model = models.Signature
        fields = {
            "when": ["exact", "gte", "lte"],
        }


class HumanName(filters.FilterSet):
    class Meta:
        model = models.HumanName
        fields = {
            "use": ["exact", "in"],
        }


class Address(filters.FilterSet):
    class Meta:
        model = models.Address
        fields = {
            "use": ["exact", "in"],
            "type": ["exact", "in"],
        }


class ContactPoint(filters.FilterSet):
    class Meta:
        model = models.ContactPoint
        fields = {
            "system": ["exact", "in"],
            "use": ["exact", "in"],
            "rank": ["exact", "gte", "lte"],
        }


class Timing(filters.FilterSet):
    class Meta:
        model = models.Timing
        fields = []


class Timing_Repeat(filters.FilterSet):
    class Meta:
        model = models.Timing_Repeat
        fields = {
            "count": ["exact", "gte", "lte"],
            "countMax": ["exact", "gte", "lte"],
            "duration": ["exact", "gte", "lte"],
            "durationMax": ["exact", "gte", "lte"],
            "durationUnit": ["exact", "in"],
            "frequency": ["exact", "gte", "lte"],
            "frequencyMax": ["exact", "gte", "lte"],
            "period": ["exact", "gte", "lte"],
            "periodMax": ["exact", "gte", "lte"],
            "periodUnit": ["exact", "in"],
            "offset": ["exact", "gte", "lte"],
        }


class Meta(filters.FilterSet):
    class Meta:
        model = models.Meta
        fields = {
            "lastUpdated": ["exact", "gte", "lte"],
        }


class ContactDetail(filters.FilterSet):
    class Meta:
        model = models.ContactDetail
        fields = []


class Contributor(filters.FilterSet):
    class Meta:
        model = models.Contributor
        fields = {
            "type": ["exact", "in"],
        }


class DataRequirement(filters.FilterSet):
    class Meta:
        model = models.DataRequirement
        fields = {
            "limit": ["exact", "gte", "lte"],
        }


class DataRequirement_CodeFilter(filters.FilterSet):
    class Meta:
        model = models.DataRequirement_CodeFilter
        fields = []


class DataRequirement_DateFilter(filters.FilterSet):
    class Meta:
        model = models.DataRequirement_DateFilter
        fields = []


class DataRequirement_Sort(filters.FilterSet):
    class Meta:
        model = models.DataRequirement_Sort
        fields = {
            "direction": ["exact", "in"],
        }


class ParameterDefinition(filters.FilterSet):
    class Meta:
        model = models.ParameterDefinition
        fields = {
            "min": ["exact", "gte", "lte"],
        }


class RelatedArtifact(filters.FilterSet):
    class Meta:
        model = models.RelatedArtifact
        fields = {
            "type": ["exact", "in"],
        }


class TriggerDefinition(filters.FilterSet):
    class Meta:
        model = models.TriggerDefinition
        fields = {
            "type": ["exact", "in"],
        }


class UsageContext(filters.FilterSet):
    class Meta:
        model = models.UsageContext
        fields = []


class Dosage(filters.FilterSet):
    class Meta:
        model = models.Dosage
        fields = {
            "sequence": ["exact", "gte", "lte"],
        }


class Dosage_DoseAndRate(filters.FilterSet):
    class Meta:
        model = models.Dosage_DoseAndRate
        fields = []


class Population(filters.FilterSet):
    class Meta:
        model = models.Population
        fields = []


class ProductShelfLife(filters.FilterSet):
    class Meta:
        model = models.ProductShelfLife
        fields = []


class ProdCharacteristic(filters.FilterSet):
    class Meta:
        model = models.ProdCharacteristic
        fields = []


class MarketingStatus(filters.FilterSet):
    class Meta:
        model = models.MarketingStatus
        fields = {
            "restoreDate": ["exact", "gte", "lte"],
        }


class SubstanceAmount(filters.FilterSet):
    class Meta:
        model = models.SubstanceAmount
        fields = []


class SubstanceAmount_ReferenceRange(filters.FilterSet):
    class Meta:
        model = models.SubstanceAmount_ReferenceRange
        fields = []


class Expression(filters.FilterSet):
    class Meta:
        model = models.Expression
        fields = {
            "language": ["exact", "in"],
        }


class ElementDefinition(filters.FilterSet):
    class Meta:
        model = models.ElementDefinition
        fields = {
            "min": ["exact", "gte", "lte"],
            "defaultValueDecimal": ["exact", "gte", "lte"],
            "defaultValueInteger": ["exact", "gte", "lte"],
            "defaultValuePositiveInt": ["exact", "gte", "lte"],
            "defaultValueUnsignedInt": ["exact", "gte", "lte"],
            "fixedDecimal": ["exact", "gte", "lte"],
            "fixedInteger": ["exact", "gte", "lte"],
            "fixedPositiveInt": ["exact", "gte", "lte"],
            "fixedUnsignedInt": ["exact", "gte", "lte"],
            "patternDecimal": ["exact", "gte", "lte"],
            "patternInteger": ["exact", "gte", "lte"],
            "patternPositiveInt": ["exact", "gte", "lte"],
            "patternUnsignedInt": ["exact", "gte", "lte"],
            "minValueDecimal": ["exact", "gte", "lte"],
            "minValueInteger": ["exact", "gte", "lte"],
            "minValuePositiveInt": ["exact", "gte", "lte"],
            "minValueUnsignedInt": ["exact", "gte", "lte"],
            "maxValueDecimal": ["exact", "gte", "lte"],
            "maxValueInteger": ["exact", "gte", "lte"],
            "maxValuePositiveInt": ["exact", "gte", "lte"],
            "maxValueUnsignedInt": ["exact", "gte", "lte"],
            "maxLength": ["exact", "gte", "lte"],
        }


class ElementDefinition_Slicing(filters.FilterSet):
    class Meta:
        model = models.ElementDefinition_Slicing
        fields = {
            "rules": ["exact", "in"],
        }


class ElementDefinition_Discriminator(filters.FilterSet):
    class Meta:
        model = models.ElementDefinition_Discriminator
        fields = {
            "type": ["exact", "in"],
        }


class ElementDefinition_Base(filters.FilterSet):
    class Meta:
        model = models.ElementDefinition_Base
        fields = {
            "min": ["exact", "gte", "lte"],
        }


class ElementDefinition_Type(filters.FilterSet):
    class Meta:
        model = models.ElementDefinition_Type
        fields = {
            "versioning": ["exact", "in"],
        }


class ElementDefinition_Example(filters.FilterSet):
    class Meta:
        model = models.ElementDefinition_Example
        fields = {
            "valueDecimal": ["exact", "gte", "lte"],
            "valueInteger": ["exact", "gte", "lte"],
            "valuePositiveInt": ["exact", "gte", "lte"],
            "valueUnsignedInt": ["exact", "gte", "lte"],
        }


class ElementDefinition_Constraint(filters.FilterSet):
    class Meta:
        model = models.ElementDefinition_Constraint
        fields = {
            "severity": ["exact", "in"],
        }


class ElementDefinition_Binding(filters.FilterSet):
    class Meta:
        model = models.ElementDefinition_Binding
        fields = {
            "strength": ["exact", "in"],
        }


class ElementDefinition_Mapping(filters.FilterSet):
    class Meta:
        model = models.ElementDefinition_Mapping
        fields = []


class Account(filters.FilterSet):
    class Meta:
        model = models.Account
        fields = {
            "status": ["exact", "in"],
        }


class Account_Coverage(filters.FilterSet):
    class Meta:
        model = models.Account_Coverage
        fields = {
            "priority": ["exact", "gte", "lte"],
        }


class Account_Guarantor(filters.FilterSet):
    class Meta:
        model = models.Account_Guarantor
        fields = []


class ActivityDefinition(filters.FilterSet):
    class Meta:
        model = models.ActivityDefinition
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
            "approvalDate": ["exact", "gte", "lte"],
            "lastReviewDate": ["exact", "gte", "lte"],
        }


class ActivityDefinition_Participant(filters.FilterSet):
    class Meta:
        model = models.ActivityDefinition_Participant
        fields = []


class ActivityDefinition_DynamicValue(filters.FilterSet):
    class Meta:
        model = models.ActivityDefinition_DynamicValue
        fields = []


class AdverseEvent(filters.FilterSet):
    class Meta:
        model = models.AdverseEvent
        fields = {
            "actuality": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
            "detected": ["exact", "gte", "lte"],
            "recordedDate": ["exact", "gte", "lte"],
        }


class AdverseEvent_SuspectEntity(filters.FilterSet):
    class Meta:
        model = models.AdverseEvent_SuspectEntity
        fields = []


class AdverseEvent_Causality(filters.FilterSet):
    class Meta:
        model = models.AdverseEvent_Causality
        fields = []


class AllergyIntolerance(filters.FilterSet):
    class Meta:
        model = models.AllergyIntolerance
        fields = {
            "type": ["exact", "in"],
            "criticality": ["exact", "in"],
            "recordedDate": ["exact", "gte", "lte"],
            "lastOccurrence": ["exact", "gte", "lte"],
        }


class AllergyIntolerance_Reaction(filters.FilterSet):
    class Meta:
        model = models.AllergyIntolerance_Reaction
        fields = {
            "onset": ["exact", "gte", "lte"],
            "severity": ["exact", "in"],
        }


class Appointment(filters.FilterSet):
    class Meta:
        model = models.Appointment
        fields = {
            "status": ["exact", "in"],
            "priority": ["exact", "gte", "lte"],
            "start": ["exact", "gte", "lte"],
            "end": ["exact", "gte", "lte"],
            "minutesDuration": ["exact", "gte", "lte"],
            "created": ["exact", "gte", "lte"],
        }


class Appointment_Participant(filters.FilterSet):
    class Meta:
        model = models.Appointment_Participant
        fields = {
            "required": ["exact", "in"],
            "status": ["exact", "in"],
        }


class AppointmentResponse(filters.FilterSet):
    class Meta:
        model = models.AppointmentResponse
        fields = {
            "start": ["exact", "gte", "lte"],
            "end": ["exact", "gte", "lte"],
        }


class AuditEvent(filters.FilterSet):
    class Meta:
        model = models.AuditEvent
        fields = {
            "action": ["exact", "in"],
            "recorded": ["exact", "gte", "lte"],
            "outcome": ["exact", "in"],
        }


class AuditEvent_Agent(filters.FilterSet):
    class Meta:
        model = models.AuditEvent_Agent
        fields = []


class AuditEvent_Network(filters.FilterSet):
    class Meta:
        model = models.AuditEvent_Network
        fields = {
            "type": ["exact", "in"],
        }


class AuditEvent_Source(filters.FilterSet):
    class Meta:
        model = models.AuditEvent_Source
        fields = []


class AuditEvent_Entity(filters.FilterSet):
    class Meta:
        model = models.AuditEvent_Entity
        fields = []


class AuditEvent_Detail(filters.FilterSet):
    class Meta:
        model = models.AuditEvent_Detail
        fields = []


class Basic(filters.FilterSet):
    class Meta:
        model = models.Basic
        fields = {
            "created": ["exact", "gte", "lte"],
        }


class Binary(filters.FilterSet):
    class Meta:
        model = models.Binary
        fields = []


class BiologicallyDerivedProduct(filters.FilterSet):
    class Meta:
        model = models.BiologicallyDerivedProduct
        fields = {
            "productCategory": ["exact", "in"],
            "status": ["exact", "in"],
            "quantity": ["exact", "gte", "lte"],
        }


class BiologicallyDerivedProduct_Collection(filters.FilterSet):
    class Meta:
        model = models.BiologicallyDerivedProduct_Collection
        fields = []


class BiologicallyDerivedProduct_Processing(filters.FilterSet):
    class Meta:
        model = models.BiologicallyDerivedProduct_Processing
        fields = []


class BiologicallyDerivedProduct_Manipulation(filters.FilterSet):
    class Meta:
        model = models.BiologicallyDerivedProduct_Manipulation
        fields = []


class BiologicallyDerivedProduct_Storage(filters.FilterSet):
    class Meta:
        model = models.BiologicallyDerivedProduct_Storage
        fields = {
            "temperature": ["exact", "gte", "lte"],
            "scale": ["exact", "in"],
        }


class BodyStructure(filters.FilterSet):
    class Meta:
        model = models.BodyStructure
        fields = []


class Bundle(filters.FilterSet):
    class Meta:
        model = models.Bundle
        fields = {
            "type": ["exact", "in"],
            "timestamp": ["exact", "gte", "lte"],
            "total": ["exact", "gte", "lte"],
        }


class Bundle_Link(filters.FilterSet):
    class Meta:
        model = models.Bundle_Link
        fields = []


class Bundle_Entry(filters.FilterSet):
    class Meta:
        model = models.Bundle_Entry
        fields = []


class Bundle_Search(filters.FilterSet):
    class Meta:
        model = models.Bundle_Search
        fields = {
            "mode": ["exact", "in"],
            "score": ["exact", "gte", "lte"],
        }


class Bundle_Request(filters.FilterSet):
    class Meta:
        model = models.Bundle_Request
        fields = {
            "method": ["exact", "in"],
            "ifModifiedSince": ["exact", "gte", "lte"],
        }


class Bundle_Response(filters.FilterSet):
    class Meta:
        model = models.Bundle_Response
        fields = {
            "lastModified": ["exact", "gte", "lte"],
        }


class CapabilityStatement(filters.FilterSet):
    class Meta:
        model = models.CapabilityStatement
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
            "kind": ["exact", "in"],
            "fhirVersion": ["exact", "in"],
        }


class CapabilityStatement_Software(filters.FilterSet):
    class Meta:
        model = models.CapabilityStatement_Software
        fields = {
            "releaseDate": ["exact", "gte", "lte"],
        }


class CapabilityStatement_Implementation(filters.FilterSet):
    class Meta:
        model = models.CapabilityStatement_Implementation
        fields = []


class CapabilityStatement_Rest(filters.FilterSet):
    class Meta:
        model = models.CapabilityStatement_Rest
        fields = {
            "mode": ["exact", "in"],
        }


class CapabilityStatement_Security(filters.FilterSet):
    class Meta:
        model = models.CapabilityStatement_Security
        fields = []


class CapabilityStatement_Resource(filters.FilterSet):
    class Meta:
        model = models.CapabilityStatement_Resource
        fields = {
            "versioning": ["exact", "in"],
            "conditionalRead": ["exact", "in"],
            "conditionalDelete": ["exact", "in"],
        }


class CapabilityStatement_Interaction(filters.FilterSet):
    class Meta:
        model = models.CapabilityStatement_Interaction
        fields = {
            "code": ["exact", "in"],
        }


class CapabilityStatement_SearchParam(filters.FilterSet):
    class Meta:
        model = models.CapabilityStatement_SearchParam
        fields = {
            "type": ["exact", "in"],
        }


class CapabilityStatement_Operation(filters.FilterSet):
    class Meta:
        model = models.CapabilityStatement_Operation
        fields = []


class CapabilityStatement_Interaction1(filters.FilterSet):
    class Meta:
        model = models.CapabilityStatement_Interaction1
        fields = {
            "code": ["exact", "in"],
        }


class CapabilityStatement_Messaging(filters.FilterSet):
    class Meta:
        model = models.CapabilityStatement_Messaging
        fields = {
            "reliableCache": ["exact", "gte", "lte"],
        }


class CapabilityStatement_Endpoint(filters.FilterSet):
    class Meta:
        model = models.CapabilityStatement_Endpoint
        fields = []


class CapabilityStatement_SupportedMessage(filters.FilterSet):
    class Meta:
        model = models.CapabilityStatement_SupportedMessage
        fields = {
            "mode": ["exact", "in"],
        }


class CapabilityStatement_Document(filters.FilterSet):
    class Meta:
        model = models.CapabilityStatement_Document
        fields = {
            "mode": ["exact", "in"],
        }


class CarePlan(filters.FilterSet):
    class Meta:
        model = models.CarePlan
        fields = {
            "created": ["exact", "gte", "lte"],
        }


class CarePlan_Activity(filters.FilterSet):
    class Meta:
        model = models.CarePlan_Activity
        fields = []


class CarePlan_Detail(filters.FilterSet):
    class Meta:
        model = models.CarePlan_Detail
        fields = {
            "status": ["exact", "in"],
        }


class CareTeam(filters.FilterSet):
    class Meta:
        model = models.CareTeam
        fields = {
            "status": ["exact", "in"],
        }


class CareTeam_Participant(filters.FilterSet):
    class Meta:
        model = models.CareTeam_Participant
        fields = []


class CatalogEntry(filters.FilterSet):
    class Meta:
        model = models.CatalogEntry
        fields = {
            "status": ["exact", "in"],
            "validTo": ["exact", "gte", "lte"],
            "lastUpdated": ["exact", "gte", "lte"],
        }


class CatalogEntry_RelatedEntry(filters.FilterSet):
    class Meta:
        model = models.CatalogEntry_RelatedEntry
        fields = {
            "relationtype": ["exact", "in"],
        }


class ChargeItem(filters.FilterSet):
    class Meta:
        model = models.ChargeItem
        fields = {
            "status": ["exact", "in"],
            "factorOverride": ["exact", "gte", "lte"],
            "enteredDate": ["exact", "gte", "lte"],
        }


class ChargeItem_Performer(filters.FilterSet):
    class Meta:
        model = models.ChargeItem_Performer
        fields = []


class ChargeItemDefinition(filters.FilterSet):
    class Meta:
        model = models.ChargeItemDefinition
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
            "approvalDate": ["exact", "gte", "lte"],
            "lastReviewDate": ["exact", "gte", "lte"],
        }


class ChargeItemDefinition_Applicability(filters.FilterSet):
    class Meta:
        model = models.ChargeItemDefinition_Applicability
        fields = []


class ChargeItemDefinition_PropertyGroup(filters.FilterSet):
    class Meta:
        model = models.ChargeItemDefinition_PropertyGroup
        fields = []


class ChargeItemDefinition_PriceComponent(filters.FilterSet):
    class Meta:
        model = models.ChargeItemDefinition_PriceComponent
        fields = {
            "factor": ["exact", "gte", "lte"],
        }


class Claim(filters.FilterSet):
    class Meta:
        model = models.Claim
        fields = {
            "use": ["exact", "in"],
            "created": ["exact", "gte", "lte"],
        }


class Claim_Related(filters.FilterSet):
    class Meta:
        model = models.Claim_Related
        fields = []


class Claim_Payee(filters.FilterSet):
    class Meta:
        model = models.Claim_Payee
        fields = []


class Claim_CareTeam(filters.FilterSet):
    class Meta:
        model = models.Claim_CareTeam
        fields = {
            "sequence": ["exact", "gte", "lte"],
        }


class Claim_SupportingInfo(filters.FilterSet):
    class Meta:
        model = models.Claim_SupportingInfo
        fields = {
            "sequence": ["exact", "gte", "lte"],
        }


class Claim_Diagnosis(filters.FilterSet):
    class Meta:
        model = models.Claim_Diagnosis
        fields = {
            "sequence": ["exact", "gte", "lte"],
        }


class Claim_Procedure(filters.FilterSet):
    class Meta:
        model = models.Claim_Procedure
        fields = {
            "sequence": ["exact", "gte", "lte"],
            "date": ["exact", "gte", "lte"],
        }


class Claim_Insurance(filters.FilterSet):
    class Meta:
        model = models.Claim_Insurance
        fields = {
            "sequence": ["exact", "gte", "lte"],
        }


class Claim_Accident(filters.FilterSet):
    class Meta:
        model = models.Claim_Accident
        fields = {
            "date": ["exact", "gte", "lte"],
        }


class Claim_Item(filters.FilterSet):
    class Meta:
        model = models.Claim_Item
        fields = {
            "sequence": ["exact", "gte", "lte"],
            "factor": ["exact", "gte", "lte"],
        }


class Claim_Detail(filters.FilterSet):
    class Meta:
        model = models.Claim_Detail
        fields = {
            "sequence": ["exact", "gte", "lte"],
            "factor": ["exact", "gte", "lte"],
        }


class Claim_SubDetail(filters.FilterSet):
    class Meta:
        model = models.Claim_SubDetail
        fields = {
            "sequence": ["exact", "gte", "lte"],
            "factor": ["exact", "gte", "lte"],
        }


class ClaimResponse(filters.FilterSet):
    class Meta:
        model = models.ClaimResponse
        fields = {
            "created": ["exact", "gte", "lte"],
        }


class ClaimResponse_Item(filters.FilterSet):
    class Meta:
        model = models.ClaimResponse_Item
        fields = {
            "itemSequence": ["exact", "gte", "lte"],
        }


class ClaimResponse_Adjudication(filters.FilterSet):
    class Meta:
        model = models.ClaimResponse_Adjudication
        fields = {
            "value": ["exact", "gte", "lte"],
        }


class ClaimResponse_Detail(filters.FilterSet):
    class Meta:
        model = models.ClaimResponse_Detail
        fields = {
            "detailSequence": ["exact", "gte", "lte"],
        }


class ClaimResponse_SubDetail(filters.FilterSet):
    class Meta:
        model = models.ClaimResponse_SubDetail
        fields = {
            "subDetailSequence": ["exact", "gte", "lte"],
        }


class ClaimResponse_AddItem(filters.FilterSet):
    class Meta:
        model = models.ClaimResponse_AddItem
        fields = {
            "factor": ["exact", "gte", "lte"],
        }


class ClaimResponse_Detail1(filters.FilterSet):
    class Meta:
        model = models.ClaimResponse_Detail1
        fields = {
            "factor": ["exact", "gte", "lte"],
        }


class ClaimResponse_SubDetail1(filters.FilterSet):
    class Meta:
        model = models.ClaimResponse_SubDetail1
        fields = {
            "factor": ["exact", "gte", "lte"],
        }


class ClaimResponse_Total(filters.FilterSet):
    class Meta:
        model = models.ClaimResponse_Total
        fields = []


class ClaimResponse_Payment(filters.FilterSet):
    class Meta:
        model = models.ClaimResponse_Payment
        fields = {
            "date": ["exact", "gte", "lte"],
        }


class ClaimResponse_ProcessNote(filters.FilterSet):
    class Meta:
        model = models.ClaimResponse_ProcessNote
        fields = {
            "number": ["exact", "gte", "lte"],
            "type": ["exact", "in"],
        }


class ClaimResponse_Insurance(filters.FilterSet):
    class Meta:
        model = models.ClaimResponse_Insurance
        fields = {
            "sequence": ["exact", "gte", "lte"],
        }


class ClaimResponse_Error(filters.FilterSet):
    class Meta:
        model = models.ClaimResponse_Error
        fields = {
            "itemSequence": ["exact", "gte", "lte"],
            "detailSequence": ["exact", "gte", "lte"],
            "subDetailSequence": ["exact", "gte", "lte"],
        }


class ClinicalImpression(filters.FilterSet):
    class Meta:
        model = models.ClinicalImpression
        fields = {
            "date": ["exact", "gte", "lte"],
        }


class ClinicalImpression_Investigation(filters.FilterSet):
    class Meta:
        model = models.ClinicalImpression_Investigation
        fields = []


class ClinicalImpression_Finding(filters.FilterSet):
    class Meta:
        model = models.ClinicalImpression_Finding
        fields = []


class CodeSystem(filters.FilterSet):
    class Meta:
        model = models.CodeSystem
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
            "hierarchyMeaning": ["exact", "in"],
            "content": ["exact", "in"],
            "count": ["exact", "gte", "lte"],
        }


class CodeSystem_Filter(filters.FilterSet):
    class Meta:
        model = models.CodeSystem_Filter
        fields = []


class CodeSystem_Property(filters.FilterSet):
    class Meta:
        model = models.CodeSystem_Property
        fields = {
            "type": ["exact", "in"],
        }


class CodeSystem_Concept(filters.FilterSet):
    class Meta:
        model = models.CodeSystem_Concept
        fields = []


class CodeSystem_Designation(filters.FilterSet):
    class Meta:
        model = models.CodeSystem_Designation
        fields = []


class CodeSystem_Property1(filters.FilterSet):
    class Meta:
        model = models.CodeSystem_Property1
        fields = {
            "valueInteger": ["exact", "gte", "lte"],
            "valueDecimal": ["exact", "gte", "lte"],
        }


class Communication(filters.FilterSet):
    class Meta:
        model = models.Communication
        fields = {
            "sent": ["exact", "gte", "lte"],
            "received": ["exact", "gte", "lte"],
        }


class Communication_Payload(filters.FilterSet):
    class Meta:
        model = models.Communication_Payload
        fields = []


class CommunicationRequest(filters.FilterSet):
    class Meta:
        model = models.CommunicationRequest
        fields = {
            "authoredOn": ["exact", "gte", "lte"],
        }


class CommunicationRequest_Payload(filters.FilterSet):
    class Meta:
        model = models.CommunicationRequest_Payload
        fields = []


class CompartmentDefinition(filters.FilterSet):
    class Meta:
        model = models.CompartmentDefinition
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
            "code": ["exact", "in"],
        }


class CompartmentDefinition_Resource(filters.FilterSet):
    class Meta:
        model = models.CompartmentDefinition_Resource
        fields = []


class Composition(filters.FilterSet):
    class Meta:
        model = models.Composition
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
        }


class Composition_Attester(filters.FilterSet):
    class Meta:
        model = models.Composition_Attester
        fields = {
            "mode": ["exact", "in"],
            "time": ["exact", "gte", "lte"],
        }


class Composition_RelatesTo(filters.FilterSet):
    class Meta:
        model = models.Composition_RelatesTo
        fields = []


class Composition_Event(filters.FilterSet):
    class Meta:
        model = models.Composition_Event
        fields = []


class Composition_Section(filters.FilterSet):
    class Meta:
        model = models.Composition_Section
        fields = []


class ConceptMap(filters.FilterSet):
    class Meta:
        model = models.ConceptMap
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
        }


class ConceptMap_Group(filters.FilterSet):
    class Meta:
        model = models.ConceptMap_Group
        fields = []


class ConceptMap_Element(filters.FilterSet):
    class Meta:
        model = models.ConceptMap_Element
        fields = []


class ConceptMap_Target(filters.FilterSet):
    class Meta:
        model = models.ConceptMap_Target
        fields = {
            "equivalence": ["exact", "in"],
        }


class ConceptMap_DependsOn(filters.FilterSet):
    class Meta:
        model = models.ConceptMap_DependsOn
        fields = []


class ConceptMap_Unmapped(filters.FilterSet):
    class Meta:
        model = models.ConceptMap_Unmapped
        fields = {
            "mode": ["exact", "in"],
        }


class Condition(filters.FilterSet):
    class Meta:
        model = models.Condition
        fields = {
            "recordedDate": ["exact", "gte", "lte"],
        }


class Condition_Stage(filters.FilterSet):
    class Meta:
        model = models.Condition_Stage
        fields = []


class Condition_Evidence(filters.FilterSet):
    class Meta:
        model = models.Condition_Evidence
        fields = []


class Consent(filters.FilterSet):
    class Meta:
        model = models.Consent
        fields = {
            "status": ["exact", "in"],
            "dateTime": ["exact", "gte", "lte"],
        }


class Consent_Policy(filters.FilterSet):
    class Meta:
        model = models.Consent_Policy
        fields = []


class Consent_Verification(filters.FilterSet):
    class Meta:
        model = models.Consent_Verification
        fields = {
            "verificationDate": ["exact", "gte", "lte"],
        }


class Consent_Provision(filters.FilterSet):
    class Meta:
        model = models.Consent_Provision
        fields = {
            "type": ["exact", "in"],
        }


class Consent_Actor(filters.FilterSet):
    class Meta:
        model = models.Consent_Actor
        fields = []


class Consent_Data(filters.FilterSet):
    class Meta:
        model = models.Consent_Data
        fields = {
            "meaning": ["exact", "in"],
        }


class Contract(filters.FilterSet):
    class Meta:
        model = models.Contract
        fields = {
            "issued": ["exact", "gte", "lte"],
        }


class Contract_ContentDefinition(filters.FilterSet):
    class Meta:
        model = models.Contract_ContentDefinition
        fields = {
            "publicationDate": ["exact", "gte", "lte"],
        }


class Contract_Term(filters.FilterSet):
    class Meta:
        model = models.Contract_Term
        fields = {
            "issued": ["exact", "gte", "lte"],
        }


class Contract_SecurityLabel(filters.FilterSet):
    class Meta:
        model = models.Contract_SecurityLabel
        fields = []


class Contract_Offer(filters.FilterSet):
    class Meta:
        model = models.Contract_Offer
        fields = []


class Contract_Party(filters.FilterSet):
    class Meta:
        model = models.Contract_Party
        fields = []


class Contract_Answer(filters.FilterSet):
    class Meta:
        model = models.Contract_Answer
        fields = {
            "valueDecimal": ["exact", "gte", "lte"],
            "valueInteger": ["exact", "gte", "lte"],
        }


class Contract_Asset(filters.FilterSet):
    class Meta:
        model = models.Contract_Asset
        fields = []


class Contract_Context(filters.FilterSet):
    class Meta:
        model = models.Contract_Context
        fields = []


class Contract_ValuedItem(filters.FilterSet):
    class Meta:
        model = models.Contract_ValuedItem
        fields = {
            "effectiveTime": ["exact", "gte", "lte"],
            "factor": ["exact", "gte", "lte"],
            "points": ["exact", "gte", "lte"],
            "paymentDate": ["exact", "gte", "lte"],
        }


class Contract_Action(filters.FilterSet):
    class Meta:
        model = models.Contract_Action
        fields = []


class Contract_Subject(filters.FilterSet):
    class Meta:
        model = models.Contract_Subject
        fields = []


class Contract_Signer(filters.FilterSet):
    class Meta:
        model = models.Contract_Signer
        fields = []


class Contract_Friendly(filters.FilterSet):
    class Meta:
        model = models.Contract_Friendly
        fields = []


class Contract_Legal(filters.FilterSet):
    class Meta:
        model = models.Contract_Legal
        fields = []


class Contract_Rule(filters.FilterSet):
    class Meta:
        model = models.Contract_Rule
        fields = []


class Coverage(filters.FilterSet):
    class Meta:
        model = models.Coverage
        fields = {
            "order": ["exact", "gte", "lte"],
        }


class Coverage_Class(filters.FilterSet):
    class Meta:
        model = models.Coverage_Class
        fields = []


class Coverage_CostToBeneficiary(filters.FilterSet):
    class Meta:
        model = models.Coverage_CostToBeneficiary
        fields = []


class Coverage_Exception(filters.FilterSet):
    class Meta:
        model = models.Coverage_Exception
        fields = []


class CoverageEligibilityRequest(filters.FilterSet):
    class Meta:
        model = models.CoverageEligibilityRequest
        fields = {
            "created": ["exact", "gte", "lte"],
        }


class CoverageEligibilityRequest_SupportingInfo(filters.FilterSet):
    class Meta:
        model = models.CoverageEligibilityRequest_SupportingInfo
        fields = {
            "sequence": ["exact", "gte", "lte"],
        }


class CoverageEligibilityRequest_Insurance(filters.FilterSet):
    class Meta:
        model = models.CoverageEligibilityRequest_Insurance
        fields = []


class CoverageEligibilityRequest_Item(filters.FilterSet):
    class Meta:
        model = models.CoverageEligibilityRequest_Item
        fields = []


class CoverageEligibilityRequest_Diagnosis(filters.FilterSet):
    class Meta:
        model = models.CoverageEligibilityRequest_Diagnosis
        fields = []


class CoverageEligibilityResponse(filters.FilterSet):
    class Meta:
        model = models.CoverageEligibilityResponse
        fields = {
            "created": ["exact", "gte", "lte"],
            "outcome": ["exact", "in"],
        }


class CoverageEligibilityResponse_Insurance(filters.FilterSet):
    class Meta:
        model = models.CoverageEligibilityResponse_Insurance
        fields = []


class CoverageEligibilityResponse_Item(filters.FilterSet):
    class Meta:
        model = models.CoverageEligibilityResponse_Item
        fields = []


class CoverageEligibilityResponse_Benefit(filters.FilterSet):
    class Meta:
        model = models.CoverageEligibilityResponse_Benefit
        fields = {
            "allowedUnsignedInt": ["exact", "gte", "lte"],
            "usedUnsignedInt": ["exact", "gte", "lte"],
        }


class CoverageEligibilityResponse_Error(filters.FilterSet):
    class Meta:
        model = models.CoverageEligibilityResponse_Error
        fields = []


class DetectedIssue(filters.FilterSet):
    class Meta:
        model = models.DetectedIssue
        fields = {
            "severity": ["exact", "in"],
        }


class DetectedIssue_Evidence(filters.FilterSet):
    class Meta:
        model = models.DetectedIssue_Evidence
        fields = []


class DetectedIssue_Mitigation(filters.FilterSet):
    class Meta:
        model = models.DetectedIssue_Mitigation
        fields = {
            "date": ["exact", "gte", "lte"],
        }


class Device(filters.FilterSet):
    class Meta:
        model = models.Device
        fields = {
            "status": ["exact", "in"],
            "manufactureDate": ["exact", "gte", "lte"],
            "expirationDate": ["exact", "gte", "lte"],
        }


class Device_UdiCarrier(filters.FilterSet):
    class Meta:
        model = models.Device_UdiCarrier
        fields = {
            "entryType": ["exact", "in"],
        }


class Device_DeviceName(filters.FilterSet):
    class Meta:
        model = models.Device_DeviceName
        fields = {
            "type": ["exact", "in"],
        }


class Device_Specialization(filters.FilterSet):
    class Meta:
        model = models.Device_Specialization
        fields = []


class Device_Version(filters.FilterSet):
    class Meta:
        model = models.Device_Version
        fields = []


class Device_Property(filters.FilterSet):
    class Meta:
        model = models.Device_Property
        fields = []


class DeviceDefinition(filters.FilterSet):
    class Meta:
        model = models.DeviceDefinition
        fields = []


class DeviceDefinition_UdiDeviceIdentifier(filters.FilterSet):
    class Meta:
        model = models.DeviceDefinition_UdiDeviceIdentifier
        fields = []


class DeviceDefinition_DeviceName(filters.FilterSet):
    class Meta:
        model = models.DeviceDefinition_DeviceName
        fields = {
            "type": ["exact", "in"],
        }


class DeviceDefinition_Specialization(filters.FilterSet):
    class Meta:
        model = models.DeviceDefinition_Specialization
        fields = []


class DeviceDefinition_Capability(filters.FilterSet):
    class Meta:
        model = models.DeviceDefinition_Capability
        fields = []


class DeviceDefinition_Property(filters.FilterSet):
    class Meta:
        model = models.DeviceDefinition_Property
        fields = []


class DeviceDefinition_Material(filters.FilterSet):
    class Meta:
        model = models.DeviceDefinition_Material
        fields = []


class DeviceMetric(filters.FilterSet):
    class Meta:
        model = models.DeviceMetric
        fields = {
            "operationalStatus": ["exact", "in"],
            "color": ["exact", "in"],
            "category": ["exact", "in"],
        }


class DeviceMetric_Calibration(filters.FilterSet):
    class Meta:
        model = models.DeviceMetric_Calibration
        fields = {
            "type": ["exact", "in"],
            "state": ["exact", "in"],
            "time": ["exact", "gte", "lte"],
        }


class DeviceRequest(filters.FilterSet):
    class Meta:
        model = models.DeviceRequest
        fields = {
            "authoredOn": ["exact", "gte", "lte"],
        }


class DeviceRequest_Parameter(filters.FilterSet):
    class Meta:
        model = models.DeviceRequest_Parameter
        fields = []


class DeviceUseStatement(filters.FilterSet):
    class Meta:
        model = models.DeviceUseStatement
        fields = {
            "status": ["exact", "in"],
            "recordedOn": ["exact", "gte", "lte"],
        }


class DiagnosticReport(filters.FilterSet):
    class Meta:
        model = models.DiagnosticReport
        fields = {
            "status": ["exact", "in"],
            "issued": ["exact", "gte", "lte"],
        }


class DiagnosticReport_Media(filters.FilterSet):
    class Meta:
        model = models.DiagnosticReport_Media
        fields = []


class DocumentManifest(filters.FilterSet):
    class Meta:
        model = models.DocumentManifest
        fields = {
            "status": ["exact", "in"],
            "created": ["exact", "gte", "lte"],
        }


class DocumentManifest_Related(filters.FilterSet):
    class Meta:
        model = models.DocumentManifest_Related
        fields = []


class DocumentReference(filters.FilterSet):
    class Meta:
        model = models.DocumentReference
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
        }


class DocumentReference_RelatesTo(filters.FilterSet):
    class Meta:
        model = models.DocumentReference_RelatesTo
        fields = {
            "code": ["exact", "in"],
        }


class DocumentReference_Content(filters.FilterSet):
    class Meta:
        model = models.DocumentReference_Content
        fields = []


class DocumentReference_Context(filters.FilterSet):
    class Meta:
        model = models.DocumentReference_Context
        fields = []


class EffectEvidenceSynthesis(filters.FilterSet):
    class Meta:
        model = models.EffectEvidenceSynthesis
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
            "approvalDate": ["exact", "gte", "lte"],
            "lastReviewDate": ["exact", "gte", "lte"],
        }


class EffectEvidenceSynthesis_SampleSize(filters.FilterSet):
    class Meta:
        model = models.EffectEvidenceSynthesis_SampleSize
        fields = {
            "numberOfStudies": ["exact", "gte", "lte"],
            "numberOfParticipants": ["exact", "gte", "lte"],
        }


class EffectEvidenceSynthesis_ResultsByExposure(filters.FilterSet):
    class Meta:
        model = models.EffectEvidenceSynthesis_ResultsByExposure
        fields = {
            "exposureState": ["exact", "in"],
        }


class EffectEvidenceSynthesis_EffectEstimate(filters.FilterSet):
    class Meta:
        model = models.EffectEvidenceSynthesis_EffectEstimate
        fields = {
            "value": ["exact", "gte", "lte"],
        }


class EffectEvidenceSynthesis_PrecisionEstimate(filters.FilterSet):
    class Meta:
        model = models.EffectEvidenceSynthesis_PrecisionEstimate
        fields = {
            "level": ["exact", "gte", "lte"],
            "from": ["exact", "gte", "lte"],
            "to": ["exact", "gte", "lte"],
        }


class EffectEvidenceSynthesis_Certainty(filters.FilterSet):
    class Meta:
        model = models.EffectEvidenceSynthesis_Certainty
        fields = []


class EffectEvidenceSynthesis_CertaintySubcomponent(filters.FilterSet):
    class Meta:
        model = models.EffectEvidenceSynthesis_CertaintySubcomponent
        fields = []


class Encounter(filters.FilterSet):
    class Meta:
        model = models.Encounter
        fields = {
            "status": ["exact", "in"],
        }


class Encounter_StatusHistory(filters.FilterSet):
    class Meta:
        model = models.Encounter_StatusHistory
        fields = {
            "status": ["exact", "in"],
        }


class Encounter_ClassHistory(filters.FilterSet):
    class Meta:
        model = models.Encounter_ClassHistory
        fields = []


class Encounter_Participant(filters.FilterSet):
    class Meta:
        model = models.Encounter_Participant
        fields = []


class Encounter_Diagnosis(filters.FilterSet):
    class Meta:
        model = models.Encounter_Diagnosis
        fields = {
            "rank": ["exact", "gte", "lte"],
        }


class Encounter_Hospitalization(filters.FilterSet):
    class Meta:
        model = models.Encounter_Hospitalization
        fields = []


class Encounter_Location(filters.FilterSet):
    class Meta:
        model = models.Encounter_Location
        fields = {
            "status": ["exact", "in"],
        }


class Endpoint(filters.FilterSet):
    class Meta:
        model = models.Endpoint
        fields = {
            "status": ["exact", "in"],
        }


class EnrollmentRequest(filters.FilterSet):
    class Meta:
        model = models.EnrollmentRequest
        fields = {
            "created": ["exact", "gte", "lte"],
        }


class EnrollmentResponse(filters.FilterSet):
    class Meta:
        model = models.EnrollmentResponse
        fields = {
            "outcome": ["exact", "in"],
            "created": ["exact", "gte", "lte"],
        }


class EpisodeOfCare(filters.FilterSet):
    class Meta:
        model = models.EpisodeOfCare
        fields = {
            "status": ["exact", "in"],
        }


class EpisodeOfCare_StatusHistory(filters.FilterSet):
    class Meta:
        model = models.EpisodeOfCare_StatusHistory
        fields = {
            "status": ["exact", "in"],
        }


class EpisodeOfCare_Diagnosis(filters.FilterSet):
    class Meta:
        model = models.EpisodeOfCare_Diagnosis
        fields = {
            "rank": ["exact", "gte", "lte"],
        }


class EventDefinition(filters.FilterSet):
    class Meta:
        model = models.EventDefinition
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
            "approvalDate": ["exact", "gte", "lte"],
            "lastReviewDate": ["exact", "gte", "lte"],
        }


class Evidence(filters.FilterSet):
    class Meta:
        model = models.Evidence
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
            "approvalDate": ["exact", "gte", "lte"],
            "lastReviewDate": ["exact", "gte", "lte"],
        }


class EvidenceVariable(filters.FilterSet):
    class Meta:
        model = models.EvidenceVariable
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
            "approvalDate": ["exact", "gte", "lte"],
            "lastReviewDate": ["exact", "gte", "lte"],
            "type": ["exact", "in"],
        }


class EvidenceVariable_Characteristic(filters.FilterSet):
    class Meta:
        model = models.EvidenceVariable_Characteristic
        fields = {
            "groupMeasure": ["exact", "in"],
        }


class ExampleScenario(filters.FilterSet):
    class Meta:
        model = models.ExampleScenario
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
        }


class ExampleScenario_Actor(filters.FilterSet):
    class Meta:
        model = models.ExampleScenario_Actor
        fields = {
            "type": ["exact", "in"],
        }


class ExampleScenario_Instance(filters.FilterSet):
    class Meta:
        model = models.ExampleScenario_Instance
        fields = []


class ExampleScenario_Version(filters.FilterSet):
    class Meta:
        model = models.ExampleScenario_Version
        fields = []


class ExampleScenario_ContainedInstance(filters.FilterSet):
    class Meta:
        model = models.ExampleScenario_ContainedInstance
        fields = []


class ExampleScenario_Process(filters.FilterSet):
    class Meta:
        model = models.ExampleScenario_Process
        fields = []


class ExampleScenario_Step(filters.FilterSet):
    class Meta:
        model = models.ExampleScenario_Step
        fields = []


class ExampleScenario_Operation(filters.FilterSet):
    class Meta:
        model = models.ExampleScenario_Operation
        fields = []


class ExampleScenario_Alternative(filters.FilterSet):
    class Meta:
        model = models.ExampleScenario_Alternative
        fields = []


class ExplanationOfBenefit(filters.FilterSet):
    class Meta:
        model = models.ExplanationOfBenefit
        fields = {
            "status": ["exact", "in"],
            "created": ["exact", "gte", "lte"],
            "precedence": ["exact", "gte", "lte"],
        }


class ExplanationOfBenefit_Related(filters.FilterSet):
    class Meta:
        model = models.ExplanationOfBenefit_Related
        fields = []


class ExplanationOfBenefit_Payee(filters.FilterSet):
    class Meta:
        model = models.ExplanationOfBenefit_Payee
        fields = []


class ExplanationOfBenefit_CareTeam(filters.FilterSet):
    class Meta:
        model = models.ExplanationOfBenefit_CareTeam
        fields = {
            "sequence": ["exact", "gte", "lte"],
        }


class ExplanationOfBenefit_SupportingInfo(filters.FilterSet):
    class Meta:
        model = models.ExplanationOfBenefit_SupportingInfo
        fields = {
            "sequence": ["exact", "gte", "lte"],
        }


class ExplanationOfBenefit_Diagnosis(filters.FilterSet):
    class Meta:
        model = models.ExplanationOfBenefit_Diagnosis
        fields = {
            "sequence": ["exact", "gte", "lte"],
        }


class ExplanationOfBenefit_Procedure(filters.FilterSet):
    class Meta:
        model = models.ExplanationOfBenefit_Procedure
        fields = {
            "sequence": ["exact", "gte", "lte"],
            "date": ["exact", "gte", "lte"],
        }


class ExplanationOfBenefit_Insurance(filters.FilterSet):
    class Meta:
        model = models.ExplanationOfBenefit_Insurance
        fields = []


class ExplanationOfBenefit_Accident(filters.FilterSet):
    class Meta:
        model = models.ExplanationOfBenefit_Accident
        fields = {
            "date": ["exact", "gte", "lte"],
        }


class ExplanationOfBenefit_Item(filters.FilterSet):
    class Meta:
        model = models.ExplanationOfBenefit_Item
        fields = {
            "sequence": ["exact", "gte", "lte"],
            "factor": ["exact", "gte", "lte"],
        }


class ExplanationOfBenefit_Adjudication(filters.FilterSet):
    class Meta:
        model = models.ExplanationOfBenefit_Adjudication
        fields = {
            "value": ["exact", "gte", "lte"],
        }


class ExplanationOfBenefit_Detail(filters.FilterSet):
    class Meta:
        model = models.ExplanationOfBenefit_Detail
        fields = {
            "sequence": ["exact", "gte", "lte"],
            "factor": ["exact", "gte", "lte"],
        }


class ExplanationOfBenefit_SubDetail(filters.FilterSet):
    class Meta:
        model = models.ExplanationOfBenefit_SubDetail
        fields = {
            "sequence": ["exact", "gte", "lte"],
            "factor": ["exact", "gte", "lte"],
        }


class ExplanationOfBenefit_AddItem(filters.FilterSet):
    class Meta:
        model = models.ExplanationOfBenefit_AddItem
        fields = {
            "factor": ["exact", "gte", "lte"],
        }


class ExplanationOfBenefit_Detail1(filters.FilterSet):
    class Meta:
        model = models.ExplanationOfBenefit_Detail1
        fields = {
            "factor": ["exact", "gte", "lte"],
        }


class ExplanationOfBenefit_SubDetail1(filters.FilterSet):
    class Meta:
        model = models.ExplanationOfBenefit_SubDetail1
        fields = {
            "factor": ["exact", "gte", "lte"],
        }


class ExplanationOfBenefit_Total(filters.FilterSet):
    class Meta:
        model = models.ExplanationOfBenefit_Total
        fields = []


class ExplanationOfBenefit_Payment(filters.FilterSet):
    class Meta:
        model = models.ExplanationOfBenefit_Payment
        fields = {
            "date": ["exact", "gte", "lte"],
        }


class ExplanationOfBenefit_ProcessNote(filters.FilterSet):
    class Meta:
        model = models.ExplanationOfBenefit_ProcessNote
        fields = {
            "number": ["exact", "gte", "lte"],
            "type": ["exact", "in"],
        }


class ExplanationOfBenefit_BenefitBalance(filters.FilterSet):
    class Meta:
        model = models.ExplanationOfBenefit_BenefitBalance
        fields = []


class ExplanationOfBenefit_Financial(filters.FilterSet):
    class Meta:
        model = models.ExplanationOfBenefit_Financial
        fields = {
            "allowedUnsignedInt": ["exact", "gte", "lte"],
            "usedUnsignedInt": ["exact", "gte", "lte"],
        }


class FamilyMemberHistory(filters.FilterSet):
    class Meta:
        model = models.FamilyMemberHistory
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
        }


class FamilyMemberHistory_Condition(filters.FilterSet):
    class Meta:
        model = models.FamilyMemberHistory_Condition
        fields = []


class Flag(filters.FilterSet):
    class Meta:
        model = models.Flag
        fields = {
            "status": ["exact", "in"],
        }


class Goal(filters.FilterSet):
    class Meta:
        model = models.Goal
        fields = {
            "lifecycleStatus": ["exact", "in"],
            "statusDate": ["exact", "gte", "lte"],
        }


class Goal_Target(filters.FilterSet):
    class Meta:
        model = models.Goal_Target
        fields = {
            "detailInteger": ["exact", "gte", "lte"],
        }


class GraphDefinition(filters.FilterSet):
    class Meta:
        model = models.GraphDefinition
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
        }


class GraphDefinition_Link(filters.FilterSet):
    class Meta:
        model = models.GraphDefinition_Link
        fields = {
            "min": ["exact", "gte", "lte"],
        }


class GraphDefinition_Target(filters.FilterSet):
    class Meta:
        model = models.GraphDefinition_Target
        fields = []


class GraphDefinition_Compartment(filters.FilterSet):
    class Meta:
        model = models.GraphDefinition_Compartment
        fields = {
            "use": ["exact", "in"],
            "rule": ["exact", "in"],
        }


class Group(filters.FilterSet):
    class Meta:
        model = models.Group
        fields = {
            "type": ["exact", "in"],
            "quantity": ["exact", "gte", "lte"],
        }


class Group_Characteristic(filters.FilterSet):
    class Meta:
        model = models.Group_Characteristic
        fields = []


class Group_Member(filters.FilterSet):
    class Meta:
        model = models.Group_Member
        fields = []


class GuidanceResponse(filters.FilterSet):
    class Meta:
        model = models.GuidanceResponse
        fields = {
            "status": ["exact", "in"],
            "occurrenceDateTime": ["exact", "gte", "lte"],
        }


class HealthcareService(filters.FilterSet):
    class Meta:
        model = models.HealthcareService
        fields = []


class HealthcareService_Eligibility(filters.FilterSet):
    class Meta:
        model = models.HealthcareService_Eligibility
        fields = []


class HealthcareService_AvailableTime(filters.FilterSet):
    class Meta:
        model = models.HealthcareService_AvailableTime
        fields = []


class HealthcareService_NotAvailable(filters.FilterSet):
    class Meta:
        model = models.HealthcareService_NotAvailable
        fields = []


class ImagingStudy(filters.FilterSet):
    class Meta:
        model = models.ImagingStudy
        fields = {
            "status": ["exact", "in"],
            "started": ["exact", "gte", "lte"],
            "numberOfSeries": ["exact", "gte", "lte"],
            "numberOfInstances": ["exact", "gte", "lte"],
        }


class ImagingStudy_Series(filters.FilterSet):
    class Meta:
        model = models.ImagingStudy_Series
        fields = {
            "number": ["exact", "gte", "lte"],
            "numberOfInstances": ["exact", "gte", "lte"],
            "started": ["exact", "gte", "lte"],
        }


class ImagingStudy_Performer(filters.FilterSet):
    class Meta:
        model = models.ImagingStudy_Performer
        fields = []


class ImagingStudy_Instance(filters.FilterSet):
    class Meta:
        model = models.ImagingStudy_Instance
        fields = {
            "number": ["exact", "gte", "lte"],
        }


class Immunization(filters.FilterSet):
    class Meta:
        model = models.Immunization
        fields = {
            "recorded": ["exact", "gte", "lte"],
            "expirationDate": ["exact", "gte", "lte"],
        }


class Immunization_Performer(filters.FilterSet):
    class Meta:
        model = models.Immunization_Performer
        fields = []


class Immunization_Education(filters.FilterSet):
    class Meta:
        model = models.Immunization_Education
        fields = {
            "publicationDate": ["exact", "gte", "lte"],
            "presentationDate": ["exact", "gte", "lte"],
        }


class Immunization_Reaction(filters.FilterSet):
    class Meta:
        model = models.Immunization_Reaction
        fields = {
            "date": ["exact", "gte", "lte"],
        }


class Immunization_ProtocolApplied(filters.FilterSet):
    class Meta:
        model = models.Immunization_ProtocolApplied
        fields = {
            "doseNumberPositiveInt": ["exact", "gte", "lte"],
            "seriesDosesPositiveInt": ["exact", "gte", "lte"],
        }


class ImmunizationEvaluation(filters.FilterSet):
    class Meta:
        model = models.ImmunizationEvaluation
        fields = {
            "date": ["exact", "gte", "lte"],
            "doseNumberPositiveInt": ["exact", "gte", "lte"],
            "seriesDosesPositiveInt": ["exact", "gte", "lte"],
        }


class ImmunizationRecommendation(filters.FilterSet):
    class Meta:
        model = models.ImmunizationRecommendation
        fields = {
            "date": ["exact", "gte", "lte"],
        }


class ImmunizationRecommendation_Recommendation(filters.FilterSet):
    class Meta:
        model = models.ImmunizationRecommendation_Recommendation
        fields = {
            "doseNumberPositiveInt": ["exact", "gte", "lte"],
            "seriesDosesPositiveInt": ["exact", "gte", "lte"],
        }


class ImmunizationRecommendation_DateCriterion(filters.FilterSet):
    class Meta:
        model = models.ImmunizationRecommendation_DateCriterion
        fields = {
            "value": ["exact", "gte", "lte"],
        }


class ImplementationGuide(filters.FilterSet):
    class Meta:
        model = models.ImplementationGuide
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
            "license": ["exact", "in"],
        }


class ImplementationGuide_DependsOn(filters.FilterSet):
    class Meta:
        model = models.ImplementationGuide_DependsOn
        fields = []


class ImplementationGuide_Global(filters.FilterSet):
    class Meta:
        model = models.ImplementationGuide_Global
        fields = []


class ImplementationGuide_Definition(filters.FilterSet):
    class Meta:
        model = models.ImplementationGuide_Definition
        fields = []


class ImplementationGuide_Grouping(filters.FilterSet):
    class Meta:
        model = models.ImplementationGuide_Grouping
        fields = []


class ImplementationGuide_Resource(filters.FilterSet):
    class Meta:
        model = models.ImplementationGuide_Resource
        fields = []


class ImplementationGuide_Page(filters.FilterSet):
    class Meta:
        model = models.ImplementationGuide_Page
        fields = {
            "generation": ["exact", "in"],
        }


class ImplementationGuide_Parameter(filters.FilterSet):
    class Meta:
        model = models.ImplementationGuide_Parameter
        fields = {
            "code": ["exact", "in"],
        }


class ImplementationGuide_Template(filters.FilterSet):
    class Meta:
        model = models.ImplementationGuide_Template
        fields = []


class ImplementationGuide_Manifest(filters.FilterSet):
    class Meta:
        model = models.ImplementationGuide_Manifest
        fields = []


class ImplementationGuide_Resource1(filters.FilterSet):
    class Meta:
        model = models.ImplementationGuide_Resource1
        fields = []


class ImplementationGuide_Page1(filters.FilterSet):
    class Meta:
        model = models.ImplementationGuide_Page1
        fields = []


class InsurancePlan(filters.FilterSet):
    class Meta:
        model = models.InsurancePlan
        fields = {
            "status": ["exact", "in"],
        }


class InsurancePlan_Contact(filters.FilterSet):
    class Meta:
        model = models.InsurancePlan_Contact
        fields = []


class InsurancePlan_Coverage(filters.FilterSet):
    class Meta:
        model = models.InsurancePlan_Coverage
        fields = []


class InsurancePlan_Benefit(filters.FilterSet):
    class Meta:
        model = models.InsurancePlan_Benefit
        fields = []


class InsurancePlan_Limit(filters.FilterSet):
    class Meta:
        model = models.InsurancePlan_Limit
        fields = []


class InsurancePlan_Plan(filters.FilterSet):
    class Meta:
        model = models.InsurancePlan_Plan
        fields = []


class InsurancePlan_GeneralCost(filters.FilterSet):
    class Meta:
        model = models.InsurancePlan_GeneralCost
        fields = {
            "groupSize": ["exact", "gte", "lte"],
        }


class InsurancePlan_SpecificCost(filters.FilterSet):
    class Meta:
        model = models.InsurancePlan_SpecificCost
        fields = []


class InsurancePlan_Benefit1(filters.FilterSet):
    class Meta:
        model = models.InsurancePlan_Benefit1
        fields = []


class InsurancePlan_Cost(filters.FilterSet):
    class Meta:
        model = models.InsurancePlan_Cost
        fields = []


class Invoice(filters.FilterSet):
    class Meta:
        model = models.Invoice
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
        }


class Invoice_Participant(filters.FilterSet):
    class Meta:
        model = models.Invoice_Participant
        fields = []


class Invoice_LineItem(filters.FilterSet):
    class Meta:
        model = models.Invoice_LineItem
        fields = {
            "sequence": ["exact", "gte", "lte"],
        }


class Invoice_PriceComponent(filters.FilterSet):
    class Meta:
        model = models.Invoice_PriceComponent
        fields = {
            "type": ["exact", "in"],
            "factor": ["exact", "gte", "lte"],
        }


class Library(filters.FilterSet):
    class Meta:
        model = models.Library
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
            "approvalDate": ["exact", "gte", "lte"],
            "lastReviewDate": ["exact", "gte", "lte"],
        }


class Linkage(filters.FilterSet):
    class Meta:
        model = models.Linkage
        fields = []


class Linkage_Item(filters.FilterSet):
    class Meta:
        model = models.Linkage_Item
        fields = {
            "type": ["exact", "in"],
        }


class List(filters.FilterSet):
    class Meta:
        model = models.List
        fields = {
            "status": ["exact", "in"],
            "mode": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
        }


class List_Entry(filters.FilterSet):
    class Meta:
        model = models.List_Entry
        fields = {
            "date": ["exact", "gte", "lte"],
        }


class Location(filters.FilterSet):
    class Meta:
        model = models.Location
        fields = {
            "status": ["exact", "in"],
            "mode": ["exact", "in"],
        }


class Location_Position(filters.FilterSet):
    class Meta:
        model = models.Location_Position
        fields = {
            "longitude": ["exact", "gte", "lte"],
            "latitude": ["exact", "gte", "lte"],
            "altitude": ["exact", "gte", "lte"],
        }


class Location_HoursOfOperation(filters.FilterSet):
    class Meta:
        model = models.Location_HoursOfOperation
        fields = []


class Measure(filters.FilterSet):
    class Meta:
        model = models.Measure
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
            "approvalDate": ["exact", "gte", "lte"],
            "lastReviewDate": ["exact", "gte", "lte"],
        }


class Measure_Group(filters.FilterSet):
    class Meta:
        model = models.Measure_Group
        fields = []


class Measure_Population(filters.FilterSet):
    class Meta:
        model = models.Measure_Population
        fields = []


class Measure_Stratifier(filters.FilterSet):
    class Meta:
        model = models.Measure_Stratifier
        fields = []


class Measure_Component(filters.FilterSet):
    class Meta:
        model = models.Measure_Component
        fields = []


class Measure_SupplementalData(filters.FilterSet):
    class Meta:
        model = models.Measure_SupplementalData
        fields = []


class MeasureReport(filters.FilterSet):
    class Meta:
        model = models.MeasureReport
        fields = {
            "status": ["exact", "in"],
            "type": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
        }


class MeasureReport_Group(filters.FilterSet):
    class Meta:
        model = models.MeasureReport_Group
        fields = []


class MeasureReport_Population(filters.FilterSet):
    class Meta:
        model = models.MeasureReport_Population
        fields = {
            "count": ["exact", "gte", "lte"],
        }


class MeasureReport_Stratifier(filters.FilterSet):
    class Meta:
        model = models.MeasureReport_Stratifier
        fields = []


class MeasureReport_Stratum(filters.FilterSet):
    class Meta:
        model = models.MeasureReport_Stratum
        fields = []


class MeasureReport_Component(filters.FilterSet):
    class Meta:
        model = models.MeasureReport_Component
        fields = []


class MeasureReport_Population1(filters.FilterSet):
    class Meta:
        model = models.MeasureReport_Population1
        fields = {
            "count": ["exact", "gte", "lte"],
        }


class Media(filters.FilterSet):
    class Meta:
        model = models.Media
        fields = {
            "issued": ["exact", "gte", "lte"],
            "height": ["exact", "gte", "lte"],
            "width": ["exact", "gte", "lte"],
            "frames": ["exact", "gte", "lte"],
            "duration": ["exact", "gte", "lte"],
        }


class Medication(filters.FilterSet):
    class Meta:
        model = models.Medication
        fields = []


class Medication_Ingredient(filters.FilterSet):
    class Meta:
        model = models.Medication_Ingredient
        fields = []


class Medication_Batch(filters.FilterSet):
    class Meta:
        model = models.Medication_Batch
        fields = {
            "expirationDate": ["exact", "gte", "lte"],
        }


class MedicationAdministration(filters.FilterSet):
    class Meta:
        model = models.MedicationAdministration
        fields = []


class MedicationAdministration_Performer(filters.FilterSet):
    class Meta:
        model = models.MedicationAdministration_Performer
        fields = []


class MedicationAdministration_Dosage(filters.FilterSet):
    class Meta:
        model = models.MedicationAdministration_Dosage
        fields = []


class MedicationDispense(filters.FilterSet):
    class Meta:
        model = models.MedicationDispense
        fields = {
            "whenPrepared": ["exact", "gte", "lte"],
            "whenHandedOver": ["exact", "gte", "lte"],
        }


class MedicationDispense_Performer(filters.FilterSet):
    class Meta:
        model = models.MedicationDispense_Performer
        fields = []


class MedicationDispense_Substitution(filters.FilterSet):
    class Meta:
        model = models.MedicationDispense_Substitution
        fields = []


class MedicationKnowledge(filters.FilterSet):
    class Meta:
        model = models.MedicationKnowledge
        fields = []


class MedicationKnowledge_RelatedMedicationKnowledge(filters.FilterSet):
    class Meta:
        model = models.MedicationKnowledge_RelatedMedicationKnowledge
        fields = []


class MedicationKnowledge_Monograph(filters.FilterSet):
    class Meta:
        model = models.MedicationKnowledge_Monograph
        fields = []


class MedicationKnowledge_Ingredient(filters.FilterSet):
    class Meta:
        model = models.MedicationKnowledge_Ingredient
        fields = []


class MedicationKnowledge_Cost(filters.FilterSet):
    class Meta:
        model = models.MedicationKnowledge_Cost
        fields = []


class MedicationKnowledge_MonitoringProgram(filters.FilterSet):
    class Meta:
        model = models.MedicationKnowledge_MonitoringProgram
        fields = []


class MedicationKnowledge_AdministrationGuidelines(filters.FilterSet):
    class Meta:
        model = models.MedicationKnowledge_AdministrationGuidelines
        fields = []


class MedicationKnowledge_Dosage(filters.FilterSet):
    class Meta:
        model = models.MedicationKnowledge_Dosage
        fields = []


class MedicationKnowledge_PatientCharacteristics(filters.FilterSet):
    class Meta:
        model = models.MedicationKnowledge_PatientCharacteristics
        fields = []


class MedicationKnowledge_MedicineClassification(filters.FilterSet):
    class Meta:
        model = models.MedicationKnowledge_MedicineClassification
        fields = []


class MedicationKnowledge_Packaging(filters.FilterSet):
    class Meta:
        model = models.MedicationKnowledge_Packaging
        fields = []


class MedicationKnowledge_DrugCharacteristic(filters.FilterSet):
    class Meta:
        model = models.MedicationKnowledge_DrugCharacteristic
        fields = []


class MedicationKnowledge_Regulatory(filters.FilterSet):
    class Meta:
        model = models.MedicationKnowledge_Regulatory
        fields = []


class MedicationKnowledge_Substitution(filters.FilterSet):
    class Meta:
        model = models.MedicationKnowledge_Substitution
        fields = []


class MedicationKnowledge_Schedule(filters.FilterSet):
    class Meta:
        model = models.MedicationKnowledge_Schedule
        fields = []


class MedicationKnowledge_MaxDispense(filters.FilterSet):
    class Meta:
        model = models.MedicationKnowledge_MaxDispense
        fields = []


class MedicationKnowledge_Kinetics(filters.FilterSet):
    class Meta:
        model = models.MedicationKnowledge_Kinetics
        fields = []


class MedicationRequest(filters.FilterSet):
    class Meta:
        model = models.MedicationRequest
        fields = {
            "authoredOn": ["exact", "gte", "lte"],
        }


class MedicationRequest_DispenseRequest(filters.FilterSet):
    class Meta:
        model = models.MedicationRequest_DispenseRequest
        fields = {
            "numberOfRepeatsAllowed": ["exact", "gte", "lte"],
        }


class MedicationRequest_InitialFill(filters.FilterSet):
    class Meta:
        model = models.MedicationRequest_InitialFill
        fields = []


class MedicationRequest_Substitution(filters.FilterSet):
    class Meta:
        model = models.MedicationRequest_Substitution
        fields = []


class MedicationStatement(filters.FilterSet):
    class Meta:
        model = models.MedicationStatement
        fields = {
            "dateAsserted": ["exact", "gte", "lte"],
        }


class MedicinalProduct(filters.FilterSet):
    class Meta:
        model = models.MedicinalProduct
        fields = []


class MedicinalProduct_Name(filters.FilterSet):
    class Meta:
        model = models.MedicinalProduct_Name
        fields = []


class MedicinalProduct_NamePart(filters.FilterSet):
    class Meta:
        model = models.MedicinalProduct_NamePart
        fields = []


class MedicinalProduct_CountryLanguage(filters.FilterSet):
    class Meta:
        model = models.MedicinalProduct_CountryLanguage
        fields = []


class MedicinalProduct_ManufacturingBusinessOperation(filters.FilterSet):
    class Meta:
        model = models.MedicinalProduct_ManufacturingBusinessOperation
        fields = {
            "effectiveDate": ["exact", "gte", "lte"],
        }


class MedicinalProduct_SpecialDesignation(filters.FilterSet):
    class Meta:
        model = models.MedicinalProduct_SpecialDesignation
        fields = {
            "date": ["exact", "gte", "lte"],
        }


class MedicinalProductAuthorization(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductAuthorization
        fields = {
            "statusDate": ["exact", "gte", "lte"],
            "restoreDate": ["exact", "gte", "lte"],
            "dateOfFirstAuthorization": ["exact", "gte", "lte"],
            "internationalBirthDate": ["exact", "gte", "lte"],
        }


class MedicinalProductAuthorization_JurisdictionalAuthorization(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductAuthorization_JurisdictionalAuthorization
        fields = []


class MedicinalProductAuthorization_Procedure(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductAuthorization_Procedure
        fields = []


class MedicinalProductContraindication(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductContraindication
        fields = []


class MedicinalProductContraindication_OtherTherapy(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductContraindication_OtherTherapy
        fields = []


class MedicinalProductIndication(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductIndication
        fields = []


class MedicinalProductIndication_OtherTherapy(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductIndication_OtherTherapy
        fields = []


class MedicinalProductIngredient(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductIngredient
        fields = []


class MedicinalProductIngredient_SpecifiedSubstance(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductIngredient_SpecifiedSubstance
        fields = []


class MedicinalProductIngredient_Strength(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductIngredient_Strength
        fields = []


class MedicinalProductIngredient_ReferenceStrength(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductIngredient_ReferenceStrength
        fields = []


class MedicinalProductIngredient_Substance(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductIngredient_Substance
        fields = []


class MedicinalProductInteraction(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductInteraction
        fields = []


class MedicinalProductInteraction_Interactant(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductInteraction_Interactant
        fields = []


class MedicinalProductManufactured(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductManufactured
        fields = []


class MedicinalProductPackaged(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductPackaged
        fields = []


class MedicinalProductPackaged_BatchIdentifier(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductPackaged_BatchIdentifier
        fields = []


class MedicinalProductPackaged_PackageItem(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductPackaged_PackageItem
        fields = []


class MedicinalProductPharmaceutical(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductPharmaceutical
        fields = []


class MedicinalProductPharmaceutical_Characteristics(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductPharmaceutical_Characteristics
        fields = []


class MedicinalProductPharmaceutical_RouteOfAdministration(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductPharmaceutical_RouteOfAdministration
        fields = []


class MedicinalProductPharmaceutical_TargetSpecies(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductPharmaceutical_TargetSpecies
        fields = []


class MedicinalProductPharmaceutical_WithdrawalPeriod(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductPharmaceutical_WithdrawalPeriod
        fields = []


class MedicinalProductUndesirableEffect(filters.FilterSet):
    class Meta:
        model = models.MedicinalProductUndesirableEffect
        fields = []


class MessageDefinition(filters.FilterSet):
    class Meta:
        model = models.MessageDefinition
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
            "category": ["exact", "in"],
            "responseRequired": ["exact", "in"],
        }


class MessageDefinition_Focus(filters.FilterSet):
    class Meta:
        model = models.MessageDefinition_Focus
        fields = {
            "min": ["exact", "gte", "lte"],
        }


class MessageDefinition_AllowedResponse(filters.FilterSet):
    class Meta:
        model = models.MessageDefinition_AllowedResponse
        fields = []


class MessageHeader(filters.FilterSet):
    class Meta:
        model = models.MessageHeader
        fields = []


class MessageHeader_Destination(filters.FilterSet):
    class Meta:
        model = models.MessageHeader_Destination
        fields = []


class MessageHeader_Source(filters.FilterSet):
    class Meta:
        model = models.MessageHeader_Source
        fields = []


class MessageHeader_Response(filters.FilterSet):
    class Meta:
        model = models.MessageHeader_Response
        fields = {
            "code": ["exact", "in"],
        }


class MolecularSequence(filters.FilterSet):
    class Meta:
        model = models.MolecularSequence
        fields = {
            "type": ["exact", "in"],
            "coordinateSystem": ["exact", "gte", "lte"],
            "readCoverage": ["exact", "gte", "lte"],
        }


class MolecularSequence_ReferenceSeq(filters.FilterSet):
    class Meta:
        model = models.MolecularSequence_ReferenceSeq
        fields = {
            "orientation": ["exact", "in"],
            "strand": ["exact", "in"],
            "windowStart": ["exact", "gte", "lte"],
            "windowEnd": ["exact", "gte", "lte"],
        }


class MolecularSequence_Variant(filters.FilterSet):
    class Meta:
        model = models.MolecularSequence_Variant
        fields = {
            "start": ["exact", "gte", "lte"],
            "end": ["exact", "gte", "lte"],
        }


class MolecularSequence_Quality(filters.FilterSet):
    class Meta:
        model = models.MolecularSequence_Quality
        fields = {
            "type": ["exact", "in"],
            "start": ["exact", "gte", "lte"],
            "end": ["exact", "gte", "lte"],
            "truthTP": ["exact", "gte", "lte"],
            "queryTP": ["exact", "gte", "lte"],
            "truthFN": ["exact", "gte", "lte"],
            "queryFP": ["exact", "gte", "lte"],
            "gtFP": ["exact", "gte", "lte"],
            "precision": ["exact", "gte", "lte"],
            "recall": ["exact", "gte", "lte"],
            "fScore": ["exact", "gte", "lte"],
        }


class MolecularSequence_Roc(filters.FilterSet):
    class Meta:
        model = models.MolecularSequence_Roc
        fields = []


class MolecularSequence_Repository(filters.FilterSet):
    class Meta:
        model = models.MolecularSequence_Repository
        fields = {
            "type": ["exact", "in"],
        }


class MolecularSequence_StructureVariant(filters.FilterSet):
    class Meta:
        model = models.MolecularSequence_StructureVariant
        fields = {
            "length": ["exact", "gte", "lte"],
        }


class MolecularSequence_Outer(filters.FilterSet):
    class Meta:
        model = models.MolecularSequence_Outer
        fields = {
            "start": ["exact", "gte", "lte"],
            "end": ["exact", "gte", "lte"],
        }


class MolecularSequence_Inner(filters.FilterSet):
    class Meta:
        model = models.MolecularSequence_Inner
        fields = {
            "start": ["exact", "gte", "lte"],
            "end": ["exact", "gte", "lte"],
        }


class NamingSystem(filters.FilterSet):
    class Meta:
        model = models.NamingSystem
        fields = {
            "status": ["exact", "in"],
            "kind": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
        }


class NamingSystem_UniqueId(filters.FilterSet):
    class Meta:
        model = models.NamingSystem_UniqueId
        fields = {
            "type": ["exact", "in"],
        }


class NutritionOrder(filters.FilterSet):
    class Meta:
        model = models.NutritionOrder
        fields = {
            "dateTime": ["exact", "gte", "lte"],
        }


class NutritionOrder_OralDiet(filters.FilterSet):
    class Meta:
        model = models.NutritionOrder_OralDiet
        fields = []


class NutritionOrder_Nutrient(filters.FilterSet):
    class Meta:
        model = models.NutritionOrder_Nutrient
        fields = []


class NutritionOrder_Texture(filters.FilterSet):
    class Meta:
        model = models.NutritionOrder_Texture
        fields = []


class NutritionOrder_Supplement(filters.FilterSet):
    class Meta:
        model = models.NutritionOrder_Supplement
        fields = []


class NutritionOrder_EnteralFormula(filters.FilterSet):
    class Meta:
        model = models.NutritionOrder_EnteralFormula
        fields = []


class NutritionOrder_Administration(filters.FilterSet):
    class Meta:
        model = models.NutritionOrder_Administration
        fields = []


class Observation(filters.FilterSet):
    class Meta:
        model = models.Observation
        fields = {
            "status": ["exact", "in"],
            "issued": ["exact", "gte", "lte"],
            "valueInteger": ["exact", "gte", "lte"],
        }


class Observation_ReferenceRange(filters.FilterSet):
    class Meta:
        model = models.Observation_ReferenceRange
        fields = []


class Observation_Component(filters.FilterSet):
    class Meta:
        model = models.Observation_Component
        fields = {
            "valueInteger": ["exact", "gte", "lte"],
        }


class ObservationDefinition(filters.FilterSet):
    class Meta:
        model = models.ObservationDefinition
        fields = []


class ObservationDefinition_QuantitativeDetails(filters.FilterSet):
    class Meta:
        model = models.ObservationDefinition_QuantitativeDetails
        fields = {
            "conversionFactor": ["exact", "gte", "lte"],
            "decimalPrecision": ["exact", "gte", "lte"],
        }


class ObservationDefinition_QualifiedInterval(filters.FilterSet):
    class Meta:
        model = models.ObservationDefinition_QualifiedInterval
        fields = {
            "category": ["exact", "in"],
            "gender": ["exact", "in"],
        }


class OperationDefinition(filters.FilterSet):
    class Meta:
        model = models.OperationDefinition
        fields = {
            "status": ["exact", "in"],
            "kind": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
        }


class OperationDefinition_Parameter(filters.FilterSet):
    class Meta:
        model = models.OperationDefinition_Parameter
        fields = {
            "use": ["exact", "in"],
            "min": ["exact", "gte", "lte"],
            "searchType": ["exact", "in"],
        }


class OperationDefinition_Binding(filters.FilterSet):
    class Meta:
        model = models.OperationDefinition_Binding
        fields = {
            "strength": ["exact", "in"],
        }


class OperationDefinition_ReferencedFrom(filters.FilterSet):
    class Meta:
        model = models.OperationDefinition_ReferencedFrom
        fields = []


class OperationDefinition_Overload(filters.FilterSet):
    class Meta:
        model = models.OperationDefinition_Overload
        fields = []


class OperationOutcome(filters.FilterSet):
    class Meta:
        model = models.OperationOutcome
        fields = []


class OperationOutcome_Issue(filters.FilterSet):
    class Meta:
        model = models.OperationOutcome_Issue
        fields = {
            "severity": ["exact", "in"],
            "code": ["exact", "in"],
        }


class Organization(filters.FilterSet):
    class Meta:
        model = models.Organization
        fields = []


class Organization_Contact(filters.FilterSet):
    class Meta:
        model = models.Organization_Contact
        fields = []


class OrganizationAffiliation(filters.FilterSet):
    class Meta:
        model = models.OrganizationAffiliation
        fields = []


class Parameters(filters.FilterSet):
    class Meta:
        model = models.Parameters
        fields = []


class Parameters_Parameter(filters.FilterSet):
    class Meta:
        model = models.Parameters_Parameter
        fields = {
            "valueDecimal": ["exact", "gte", "lte"],
            "valueInteger": ["exact", "gte", "lte"],
            "valuePositiveInt": ["exact", "gte", "lte"],
            "valueUnsignedInt": ["exact", "gte", "lte"],
        }


class Patient(filters.FilterSet):
    class Meta:
        model = models.Patient
        fields = {
            "gender": ["exact", "in"],
            "birthDate": ["exact", "gte", "lte"],
            "multipleBirthInteger": ["exact", "gte", "lte"],
        }


class Patient_Contact(filters.FilterSet):
    class Meta:
        model = models.Patient_Contact
        fields = {
            "gender": ["exact", "in"],
        }


class Patient_Communication(filters.FilterSet):
    class Meta:
        model = models.Patient_Communication
        fields = []


class Patient_Link(filters.FilterSet):
    class Meta:
        model = models.Patient_Link
        fields = {
            "type": ["exact", "in"],
        }


class PaymentNotice(filters.FilterSet):
    class Meta:
        model = models.PaymentNotice
        fields = {
            "created": ["exact", "gte", "lte"],
            "paymentDate": ["exact", "gte", "lte"],
        }


class PaymentReconciliation(filters.FilterSet):
    class Meta:
        model = models.PaymentReconciliation
        fields = {
            "created": ["exact", "gte", "lte"],
            "outcome": ["exact", "in"],
            "paymentDate": ["exact", "gte", "lte"],
        }


class PaymentReconciliation_Detail(filters.FilterSet):
    class Meta:
        model = models.PaymentReconciliation_Detail
        fields = {
            "date": ["exact", "gte", "lte"],
        }


class PaymentReconciliation_ProcessNote(filters.FilterSet):
    class Meta:
        model = models.PaymentReconciliation_ProcessNote
        fields = {
            "type": ["exact", "in"],
        }


class Person(filters.FilterSet):
    class Meta:
        model = models.Person
        fields = {
            "gender": ["exact", "in"],
            "birthDate": ["exact", "gte", "lte"],
        }


class Person_Link(filters.FilterSet):
    class Meta:
        model = models.Person_Link
        fields = {
            "assurance": ["exact", "in"],
        }


class PlanDefinition(filters.FilterSet):
    class Meta:
        model = models.PlanDefinition
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
            "approvalDate": ["exact", "gte", "lte"],
            "lastReviewDate": ["exact", "gte", "lte"],
        }


class PlanDefinition_Goal(filters.FilterSet):
    class Meta:
        model = models.PlanDefinition_Goal
        fields = []


class PlanDefinition_Target(filters.FilterSet):
    class Meta:
        model = models.PlanDefinition_Target
        fields = []


class PlanDefinition_Action(filters.FilterSet):
    class Meta:
        model = models.PlanDefinition_Action
        fields = {
            "groupingBehavior": ["exact", "in"],
            "selectionBehavior": ["exact", "in"],
            "requiredBehavior": ["exact", "in"],
            "precheckBehavior": ["exact", "in"],
            "cardinalityBehavior": ["exact", "in"],
        }


class PlanDefinition_Condition(filters.FilterSet):
    class Meta:
        model = models.PlanDefinition_Condition
        fields = {
            "kind": ["exact", "in"],
        }


class PlanDefinition_RelatedAction(filters.FilterSet):
    class Meta:
        model = models.PlanDefinition_RelatedAction
        fields = {
            "relationship": ["exact", "in"],
        }


class PlanDefinition_Participant(filters.FilterSet):
    class Meta:
        model = models.PlanDefinition_Participant
        fields = {
            "type": ["exact", "in"],
        }


class PlanDefinition_DynamicValue(filters.FilterSet):
    class Meta:
        model = models.PlanDefinition_DynamicValue
        fields = []


class Practitioner(filters.FilterSet):
    class Meta:
        model = models.Practitioner
        fields = {
            "gender": ["exact", "in"],
            "birthDate": ["exact", "gte", "lte"],
        }


class Practitioner_Qualification(filters.FilterSet):
    class Meta:
        model = models.Practitioner_Qualification
        fields = []


class PractitionerRole(filters.FilterSet):
    class Meta:
        model = models.PractitionerRole
        fields = []


class PractitionerRole_AvailableTime(filters.FilterSet):
    class Meta:
        model = models.PractitionerRole_AvailableTime
        fields = []


class PractitionerRole_NotAvailable(filters.FilterSet):
    class Meta:
        model = models.PractitionerRole_NotAvailable
        fields = []


class Procedure(filters.FilterSet):
    class Meta:
        model = models.Procedure
        fields = []


class Procedure_Performer(filters.FilterSet):
    class Meta:
        model = models.Procedure_Performer
        fields = []


class Procedure_FocalDevice(filters.FilterSet):
    class Meta:
        model = models.Procedure_FocalDevice
        fields = []


class Provenance(filters.FilterSet):
    class Meta:
        model = models.Provenance
        fields = {
            "recorded": ["exact", "gte", "lte"],
        }


class Provenance_Agent(filters.FilterSet):
    class Meta:
        model = models.Provenance_Agent
        fields = []


class Provenance_Entity(filters.FilterSet):
    class Meta:
        model = models.Provenance_Entity
        fields = {
            "role": ["exact", "in"],
        }


class Questionnaire(filters.FilterSet):
    class Meta:
        model = models.Questionnaire
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
            "approvalDate": ["exact", "gte", "lte"],
            "lastReviewDate": ["exact", "gte", "lte"],
        }


class Questionnaire_Item(filters.FilterSet):
    class Meta:
        model = models.Questionnaire_Item
        fields = {
            "type": ["exact", "in"],
            "enableBehavior": ["exact", "in"],
            "maxLength": ["exact", "gte", "lte"],
        }


class Questionnaire_EnableWhen(filters.FilterSet):
    class Meta:
        model = models.Questionnaire_EnableWhen
        fields = {
            "operator": ["exact", "in"],
            "answerDecimal": ["exact", "gte", "lte"],
            "answerInteger": ["exact", "gte", "lte"],
        }


class Questionnaire_AnswerOption(filters.FilterSet):
    class Meta:
        model = models.Questionnaire_AnswerOption
        fields = {
            "valueInteger": ["exact", "gte", "lte"],
        }


class Questionnaire_Initial(filters.FilterSet):
    class Meta:
        model = models.Questionnaire_Initial
        fields = {
            "valueDecimal": ["exact", "gte", "lte"],
            "valueInteger": ["exact", "gte", "lte"],
        }


class QuestionnaireResponse(filters.FilterSet):
    class Meta:
        model = models.QuestionnaireResponse
        fields = {
            "status": ["exact", "in"],
            "authored": ["exact", "gte", "lte"],
        }


class QuestionnaireResponse_Item(filters.FilterSet):
    class Meta:
        model = models.QuestionnaireResponse_Item
        fields = []


class QuestionnaireResponse_Answer(filters.FilterSet):
    class Meta:
        model = models.QuestionnaireResponse_Answer
        fields = {
            "valueDecimal": ["exact", "gte", "lte"],
            "valueInteger": ["exact", "gte", "lte"],
        }


class RelatedPerson(filters.FilterSet):
    class Meta:
        model = models.RelatedPerson
        fields = {
            "gender": ["exact", "in"],
            "birthDate": ["exact", "gte", "lte"],
        }


class RelatedPerson_Communication(filters.FilterSet):
    class Meta:
        model = models.RelatedPerson_Communication
        fields = []


class RequestGroup(filters.FilterSet):
    class Meta:
        model = models.RequestGroup
        fields = {
            "authoredOn": ["exact", "gte", "lte"],
        }


class RequestGroup_Action(filters.FilterSet):
    class Meta:
        model = models.RequestGroup_Action
        fields = []


class RequestGroup_Condition(filters.FilterSet):
    class Meta:
        model = models.RequestGroup_Condition
        fields = []


class RequestGroup_RelatedAction(filters.FilterSet):
    class Meta:
        model = models.RequestGroup_RelatedAction
        fields = []


class ResearchDefinition(filters.FilterSet):
    class Meta:
        model = models.ResearchDefinition
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
            "approvalDate": ["exact", "gte", "lte"],
            "lastReviewDate": ["exact", "gte", "lte"],
        }


class ResearchElementDefinition(filters.FilterSet):
    class Meta:
        model = models.ResearchElementDefinition
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
            "approvalDate": ["exact", "gte", "lte"],
            "lastReviewDate": ["exact", "gte", "lte"],
            "type": ["exact", "in"],
            "variableType": ["exact", "in"],
        }


class ResearchElementDefinition_Characteristic(filters.FilterSet):
    class Meta:
        model = models.ResearchElementDefinition_Characteristic
        fields = {
            "studyEffectiveGroupMeasure": ["exact", "in"],
            "participantEffectiveGroupMeasure": ["exact", "in"],
        }


class ResearchStudy(filters.FilterSet):
    class Meta:
        model = models.ResearchStudy
        fields = {
            "status": ["exact", "in"],
        }


class ResearchStudy_Arm(filters.FilterSet):
    class Meta:
        model = models.ResearchStudy_Arm
        fields = []


class ResearchStudy_Objective(filters.FilterSet):
    class Meta:
        model = models.ResearchStudy_Objective
        fields = []


class ResearchSubject(filters.FilterSet):
    class Meta:
        model = models.ResearchSubject
        fields = {
            "status": ["exact", "in"],
        }


class RiskAssessment(filters.FilterSet):
    class Meta:
        model = models.RiskAssessment
        fields = []


class RiskAssessment_Prediction(filters.FilterSet):
    class Meta:
        model = models.RiskAssessment_Prediction
        fields = {
            "probabilityDecimal": ["exact", "gte", "lte"],
            "relativeRisk": ["exact", "gte", "lte"],
        }


class RiskEvidenceSynthesis(filters.FilterSet):
    class Meta:
        model = models.RiskEvidenceSynthesis
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
            "approvalDate": ["exact", "gte", "lte"],
            "lastReviewDate": ["exact", "gte", "lte"],
        }


class RiskEvidenceSynthesis_SampleSize(filters.FilterSet):
    class Meta:
        model = models.RiskEvidenceSynthesis_SampleSize
        fields = {
            "numberOfStudies": ["exact", "gte", "lte"],
            "numberOfParticipants": ["exact", "gte", "lte"],
        }


class RiskEvidenceSynthesis_RiskEstimate(filters.FilterSet):
    class Meta:
        model = models.RiskEvidenceSynthesis_RiskEstimate
        fields = {
            "value": ["exact", "gte", "lte"],
            "denominatorCount": ["exact", "gte", "lte"],
            "numeratorCount": ["exact", "gte", "lte"],
        }


class RiskEvidenceSynthesis_PrecisionEstimate(filters.FilterSet):
    class Meta:
        model = models.RiskEvidenceSynthesis_PrecisionEstimate
        fields = {
            "level": ["exact", "gte", "lte"],
            "from": ["exact", "gte", "lte"],
            "to": ["exact", "gte", "lte"],
        }


class RiskEvidenceSynthesis_Certainty(filters.FilterSet):
    class Meta:
        model = models.RiskEvidenceSynthesis_Certainty
        fields = []


class RiskEvidenceSynthesis_CertaintySubcomponent(filters.FilterSet):
    class Meta:
        model = models.RiskEvidenceSynthesis_CertaintySubcomponent
        fields = []


class Schedule(filters.FilterSet):
    class Meta:
        model = models.Schedule
        fields = []


class SearchParameter(filters.FilterSet):
    class Meta:
        model = models.SearchParameter
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
            "type": ["exact", "in"],
            "xpathUsage": ["exact", "in"],
        }


class SearchParameter_Component(filters.FilterSet):
    class Meta:
        model = models.SearchParameter_Component
        fields = []


class ServiceRequest(filters.FilterSet):
    class Meta:
        model = models.ServiceRequest
        fields = {
            "authoredOn": ["exact", "gte", "lte"],
        }


class Slot(filters.FilterSet):
    class Meta:
        model = models.Slot
        fields = {
            "status": ["exact", "in"],
            "start": ["exact", "gte", "lte"],
            "end": ["exact", "gte", "lte"],
        }


class Specimen(filters.FilterSet):
    class Meta:
        model = models.Specimen
        fields = {
            "status": ["exact", "in"],
            "receivedTime": ["exact", "gte", "lte"],
        }


class Specimen_Collection(filters.FilterSet):
    class Meta:
        model = models.Specimen_Collection
        fields = []


class Specimen_Processing(filters.FilterSet):
    class Meta:
        model = models.Specimen_Processing
        fields = []


class Specimen_Container(filters.FilterSet):
    class Meta:
        model = models.Specimen_Container
        fields = []


class SpecimenDefinition(filters.FilterSet):
    class Meta:
        model = models.SpecimenDefinition
        fields = []


class SpecimenDefinition_TypeTested(filters.FilterSet):
    class Meta:
        model = models.SpecimenDefinition_TypeTested
        fields = {
            "preference": ["exact", "in"],
        }


class SpecimenDefinition_Container(filters.FilterSet):
    class Meta:
        model = models.SpecimenDefinition_Container
        fields = []


class SpecimenDefinition_Additive(filters.FilterSet):
    class Meta:
        model = models.SpecimenDefinition_Additive
        fields = []


class SpecimenDefinition_Handling(filters.FilterSet):
    class Meta:
        model = models.SpecimenDefinition_Handling
        fields = []


class StructureDefinition(filters.FilterSet):
    class Meta:
        model = models.StructureDefinition
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
            "fhirVersion": ["exact", "in"],
            "kind": ["exact", "in"],
            "derivation": ["exact", "in"],
        }


class StructureDefinition_Mapping(filters.FilterSet):
    class Meta:
        model = models.StructureDefinition_Mapping
        fields = []


class StructureDefinition_Context(filters.FilterSet):
    class Meta:
        model = models.StructureDefinition_Context
        fields = {
            "type": ["exact", "in"],
        }


class StructureDefinition_Snapshot(filters.FilterSet):
    class Meta:
        model = models.StructureDefinition_Snapshot
        fields = []


class StructureDefinition_Differential(filters.FilterSet):
    class Meta:
        model = models.StructureDefinition_Differential
        fields = []


class StructureMap(filters.FilterSet):
    class Meta:
        model = models.StructureMap
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
        }


class StructureMap_Structure(filters.FilterSet):
    class Meta:
        model = models.StructureMap_Structure
        fields = {
            "mode": ["exact", "in"],
        }


class StructureMap_Group(filters.FilterSet):
    class Meta:
        model = models.StructureMap_Group
        fields = {
            "typeMode": ["exact", "in"],
        }


class StructureMap_Input(filters.FilterSet):
    class Meta:
        model = models.StructureMap_Input
        fields = {
            "mode": ["exact", "in"],
        }


class StructureMap_Rule(filters.FilterSet):
    class Meta:
        model = models.StructureMap_Rule
        fields = []


class StructureMap_Source(filters.FilterSet):
    class Meta:
        model = models.StructureMap_Source
        fields = {
            "min": ["exact", "gte", "lte"],
            "defaultValueDecimal": ["exact", "gte", "lte"],
            "defaultValueInteger": ["exact", "gte", "lte"],
            "defaultValuePositiveInt": ["exact", "gte", "lte"],
            "defaultValueUnsignedInt": ["exact", "gte", "lte"],
            "listMode": ["exact", "in"],
        }


class StructureMap_Target(filters.FilterSet):
    class Meta:
        model = models.StructureMap_Target
        fields = {
            "contextType": ["exact", "in"],
            "transform": ["exact", "in"],
        }


class StructureMap_Parameter(filters.FilterSet):
    class Meta:
        model = models.StructureMap_Parameter
        fields = {
            "valueInteger": ["exact", "gte", "lte"],
            "valueDecimal": ["exact", "gte", "lte"],
        }


class StructureMap_Dependent(filters.FilterSet):
    class Meta:
        model = models.StructureMap_Dependent
        fields = []


class Subscription(filters.FilterSet):
    class Meta:
        model = models.Subscription
        fields = {
            "status": ["exact", "in"],
            "end": ["exact", "gte", "lte"],
        }


class Subscription_Channel(filters.FilterSet):
    class Meta:
        model = models.Subscription_Channel
        fields = {
            "type": ["exact", "in"],
        }


class Substance(filters.FilterSet):
    class Meta:
        model = models.Substance
        fields = {
            "status": ["exact", "in"],
        }


class Substance_Instance(filters.FilterSet):
    class Meta:
        model = models.Substance_Instance
        fields = {
            "expiry": ["exact", "gte", "lte"],
        }


class Substance_Ingredient(filters.FilterSet):
    class Meta:
        model = models.Substance_Ingredient
        fields = []


class SubstanceNucleicAcid(filters.FilterSet):
    class Meta:
        model = models.SubstanceNucleicAcid
        fields = {
            "numberOfSubunits": ["exact", "gte", "lte"],
        }


class SubstanceNucleicAcid_Subunit(filters.FilterSet):
    class Meta:
        model = models.SubstanceNucleicAcid_Subunit
        fields = {
            "subunit": ["exact", "gte", "lte"],
            "length": ["exact", "gte", "lte"],
        }


class SubstanceNucleicAcid_Linkage(filters.FilterSet):
    class Meta:
        model = models.SubstanceNucleicAcid_Linkage
        fields = []


class SubstanceNucleicAcid_Sugar(filters.FilterSet):
    class Meta:
        model = models.SubstanceNucleicAcid_Sugar
        fields = []


class SubstancePolymer(filters.FilterSet):
    class Meta:
        model = models.SubstancePolymer
        fields = []


class SubstancePolymer_MonomerSet(filters.FilterSet):
    class Meta:
        model = models.SubstancePolymer_MonomerSet
        fields = []


class SubstancePolymer_StartingMaterial(filters.FilterSet):
    class Meta:
        model = models.SubstancePolymer_StartingMaterial
        fields = []


class SubstancePolymer_Repeat(filters.FilterSet):
    class Meta:
        model = models.SubstancePolymer_Repeat
        fields = {
            "numberOfUnits": ["exact", "gte", "lte"],
        }


class SubstancePolymer_RepeatUnit(filters.FilterSet):
    class Meta:
        model = models.SubstancePolymer_RepeatUnit
        fields = []


class SubstancePolymer_DegreeOfPolymerisation(filters.FilterSet):
    class Meta:
        model = models.SubstancePolymer_DegreeOfPolymerisation
        fields = []


class SubstancePolymer_StructuralRepresentation(filters.FilterSet):
    class Meta:
        model = models.SubstancePolymer_StructuralRepresentation
        fields = []


class SubstanceProtein(filters.FilterSet):
    class Meta:
        model = models.SubstanceProtein
        fields = {
            "numberOfSubunits": ["exact", "gte", "lte"],
        }


class SubstanceProtein_Subunit(filters.FilterSet):
    class Meta:
        model = models.SubstanceProtein_Subunit
        fields = {
            "subunit": ["exact", "gte", "lte"],
            "length": ["exact", "gte", "lte"],
        }


class SubstanceReferenceInformation(filters.FilterSet):
    class Meta:
        model = models.SubstanceReferenceInformation
        fields = []


class SubstanceReferenceInformation_Gene(filters.FilterSet):
    class Meta:
        model = models.SubstanceReferenceInformation_Gene
        fields = []


class SubstanceReferenceInformation_GeneElement(filters.FilterSet):
    class Meta:
        model = models.SubstanceReferenceInformation_GeneElement
        fields = []


class SubstanceReferenceInformation_Classification(filters.FilterSet):
    class Meta:
        model = models.SubstanceReferenceInformation_Classification
        fields = []


class SubstanceReferenceInformation_Target(filters.FilterSet):
    class Meta:
        model = models.SubstanceReferenceInformation_Target
        fields = []


class SubstanceSourceMaterial(filters.FilterSet):
    class Meta:
        model = models.SubstanceSourceMaterial
        fields = []


class SubstanceSourceMaterial_FractionDescription(filters.FilterSet):
    class Meta:
        model = models.SubstanceSourceMaterial_FractionDescription
        fields = []


class SubstanceSourceMaterial_Organism(filters.FilterSet):
    class Meta:
        model = models.SubstanceSourceMaterial_Organism
        fields = []


class SubstanceSourceMaterial_Author(filters.FilterSet):
    class Meta:
        model = models.SubstanceSourceMaterial_Author
        fields = []


class SubstanceSourceMaterial_Hybrid(filters.FilterSet):
    class Meta:
        model = models.SubstanceSourceMaterial_Hybrid
        fields = []


class SubstanceSourceMaterial_OrganismGeneral(filters.FilterSet):
    class Meta:
        model = models.SubstanceSourceMaterial_OrganismGeneral
        fields = []


class SubstanceSourceMaterial_PartDescription(filters.FilterSet):
    class Meta:
        model = models.SubstanceSourceMaterial_PartDescription
        fields = []


class SubstanceSpecification(filters.FilterSet):
    class Meta:
        model = models.SubstanceSpecification
        fields = []


class SubstanceSpecification_Moiety(filters.FilterSet):
    class Meta:
        model = models.SubstanceSpecification_Moiety
        fields = []


class SubstanceSpecification_Property(filters.FilterSet):
    class Meta:
        model = models.SubstanceSpecification_Property
        fields = []


class SubstanceSpecification_Structure(filters.FilterSet):
    class Meta:
        model = models.SubstanceSpecification_Structure
        fields = []


class SubstanceSpecification_Isotope(filters.FilterSet):
    class Meta:
        model = models.SubstanceSpecification_Isotope
        fields = []


class SubstanceSpecification_MolecularWeight(filters.FilterSet):
    class Meta:
        model = models.SubstanceSpecification_MolecularWeight
        fields = []


class SubstanceSpecification_Representation(filters.FilterSet):
    class Meta:
        model = models.SubstanceSpecification_Representation
        fields = []


class SubstanceSpecification_Code(filters.FilterSet):
    class Meta:
        model = models.SubstanceSpecification_Code
        fields = {
            "statusDate": ["exact", "gte", "lte"],
        }


class SubstanceSpecification_Name(filters.FilterSet):
    class Meta:
        model = models.SubstanceSpecification_Name
        fields = []


class SubstanceSpecification_Official(filters.FilterSet):
    class Meta:
        model = models.SubstanceSpecification_Official
        fields = {
            "date": ["exact", "gte", "lte"],
        }


class SubstanceSpecification_Relationship(filters.FilterSet):
    class Meta:
        model = models.SubstanceSpecification_Relationship
        fields = []


class SupplyDelivery(filters.FilterSet):
    class Meta:
        model = models.SupplyDelivery
        fields = {
            "status": ["exact", "in"],
        }


class SupplyDelivery_SuppliedItem(filters.FilterSet):
    class Meta:
        model = models.SupplyDelivery_SuppliedItem
        fields = []


class SupplyRequest(filters.FilterSet):
    class Meta:
        model = models.SupplyRequest
        fields = {
            "status": ["exact", "in"],
            "authoredOn": ["exact", "gte", "lte"],
        }


class SupplyRequest_Parameter(filters.FilterSet):
    class Meta:
        model = models.SupplyRequest_Parameter
        fields = []


class Task(filters.FilterSet):
    class Meta:
        model = models.Task
        fields = {
            "status": ["exact", "in"],
            "intent": ["exact", "in"],
            "authoredOn": ["exact", "gte", "lte"],
            "lastModified": ["exact", "gte", "lte"],
        }


class Task_Restriction(filters.FilterSet):
    class Meta:
        model = models.Task_Restriction
        fields = {
            "repetitions": ["exact", "gte", "lte"],
        }


class Task_Input(filters.FilterSet):
    class Meta:
        model = models.Task_Input
        fields = {
            "valueDecimal": ["exact", "gte", "lte"],
            "valueInteger": ["exact", "gte", "lte"],
            "valuePositiveInt": ["exact", "gte", "lte"],
            "valueUnsignedInt": ["exact", "gte", "lte"],
        }


class Task_Output(filters.FilterSet):
    class Meta:
        model = models.Task_Output
        fields = {
            "valueDecimal": ["exact", "gte", "lte"],
            "valueInteger": ["exact", "gte", "lte"],
            "valuePositiveInt": ["exact", "gte", "lte"],
            "valueUnsignedInt": ["exact", "gte", "lte"],
        }


class TerminologyCapabilities(filters.FilterSet):
    class Meta:
        model = models.TerminologyCapabilities
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
            "codeSearch": ["exact", "in"],
        }


class TerminologyCapabilities_Software(filters.FilterSet):
    class Meta:
        model = models.TerminologyCapabilities_Software
        fields = []


class TerminologyCapabilities_Implementation(filters.FilterSet):
    class Meta:
        model = models.TerminologyCapabilities_Implementation
        fields = []


class TerminologyCapabilities_CodeSystem(filters.FilterSet):
    class Meta:
        model = models.TerminologyCapabilities_CodeSystem
        fields = []


class TerminologyCapabilities_Version(filters.FilterSet):
    class Meta:
        model = models.TerminologyCapabilities_Version
        fields = []


class TerminologyCapabilities_Filter(filters.FilterSet):
    class Meta:
        model = models.TerminologyCapabilities_Filter
        fields = []


class TerminologyCapabilities_Expansion(filters.FilterSet):
    class Meta:
        model = models.TerminologyCapabilities_Expansion
        fields = []


class TerminologyCapabilities_Parameter(filters.FilterSet):
    class Meta:
        model = models.TerminologyCapabilities_Parameter
        fields = []


class TerminologyCapabilities_ValidateCode(filters.FilterSet):
    class Meta:
        model = models.TerminologyCapabilities_ValidateCode
        fields = []


class TerminologyCapabilities_Translation(filters.FilterSet):
    class Meta:
        model = models.TerminologyCapabilities_Translation
        fields = []


class TerminologyCapabilities_Closure(filters.FilterSet):
    class Meta:
        model = models.TerminologyCapabilities_Closure
        fields = []


class TestReport(filters.FilterSet):
    class Meta:
        model = models.TestReport
        fields = {
            "status": ["exact", "in"],
            "result": ["exact", "in"],
            "score": ["exact", "gte", "lte"],
            "issued": ["exact", "gte", "lte"],
        }


class TestReport_Participant(filters.FilterSet):
    class Meta:
        model = models.TestReport_Participant
        fields = {
            "type": ["exact", "in"],
        }


class TestReport_Setup(filters.FilterSet):
    class Meta:
        model = models.TestReport_Setup
        fields = []


class TestReport_Action(filters.FilterSet):
    class Meta:
        model = models.TestReport_Action
        fields = []


class TestReport_Operation(filters.FilterSet):
    class Meta:
        model = models.TestReport_Operation
        fields = {
            "result": ["exact", "in"],
        }


class TestReport_Assert(filters.FilterSet):
    class Meta:
        model = models.TestReport_Assert
        fields = {
            "result": ["exact", "in"],
        }


class TestReport_Test(filters.FilterSet):
    class Meta:
        model = models.TestReport_Test
        fields = []


class TestReport_Action1(filters.FilterSet):
    class Meta:
        model = models.TestReport_Action1
        fields = []


class TestReport_Teardown(filters.FilterSet):
    class Meta:
        model = models.TestReport_Teardown
        fields = []


class TestReport_Action2(filters.FilterSet):
    class Meta:
        model = models.TestReport_Action2
        fields = []


class TestScript(filters.FilterSet):
    class Meta:
        model = models.TestScript
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
        }


class TestScript_Origin(filters.FilterSet):
    class Meta:
        model = models.TestScript_Origin
        fields = {
            "index": ["exact", "gte", "lte"],
        }


class TestScript_Destination(filters.FilterSet):
    class Meta:
        model = models.TestScript_Destination
        fields = {
            "index": ["exact", "gte", "lte"],
        }


class TestScript_Metadata(filters.FilterSet):
    class Meta:
        model = models.TestScript_Metadata
        fields = []


class TestScript_Link(filters.FilterSet):
    class Meta:
        model = models.TestScript_Link
        fields = []


class TestScript_Capability(filters.FilterSet):
    class Meta:
        model = models.TestScript_Capability
        fields = {
            "destination": ["exact", "gte", "lte"],
        }


class TestScript_Fixture(filters.FilterSet):
    class Meta:
        model = models.TestScript_Fixture
        fields = []


class TestScript_Variable(filters.FilterSet):
    class Meta:
        model = models.TestScript_Variable
        fields = []


class TestScript_Setup(filters.FilterSet):
    class Meta:
        model = models.TestScript_Setup
        fields = []


class TestScript_Action(filters.FilterSet):
    class Meta:
        model = models.TestScript_Action
        fields = []


class TestScript_Operation(filters.FilterSet):
    class Meta:
        model = models.TestScript_Operation
        fields = {
            "destination": ["exact", "gte", "lte"],
            "method": ["exact", "in"],
            "origin": ["exact", "gte", "lte"],
        }


class TestScript_RequestHeader(filters.FilterSet):
    class Meta:
        model = models.TestScript_RequestHeader
        fields = []


class TestScript_Assert(filters.FilterSet):
    class Meta:
        model = models.TestScript_Assert
        fields = {
            "direction": ["exact", "in"],
            "operator": ["exact", "in"],
            "requestMethod": ["exact", "in"],
            "response": ["exact", "in"],
        }


class TestScript_Test(filters.FilterSet):
    class Meta:
        model = models.TestScript_Test
        fields = []


class TestScript_Action1(filters.FilterSet):
    class Meta:
        model = models.TestScript_Action1
        fields = []


class TestScript_Teardown(filters.FilterSet):
    class Meta:
        model = models.TestScript_Teardown
        fields = []


class TestScript_Action2(filters.FilterSet):
    class Meta:
        model = models.TestScript_Action2
        fields = []


class ValueSet(filters.FilterSet):
    class Meta:
        model = models.ValueSet
        fields = {
            "status": ["exact", "in"],
            "date": ["exact", "gte", "lte"],
        }


class ValueSet_Compose(filters.FilterSet):
    class Meta:
        model = models.ValueSet_Compose
        fields = {
            "lockedDate": ["exact", "gte", "lte"],
        }


class ValueSet_Include(filters.FilterSet):
    class Meta:
        model = models.ValueSet_Include
        fields = []


class ValueSet_Concept(filters.FilterSet):
    class Meta:
        model = models.ValueSet_Concept
        fields = []


class ValueSet_Designation(filters.FilterSet):
    class Meta:
        model = models.ValueSet_Designation
        fields = []


class ValueSet_Filter(filters.FilterSet):
    class Meta:
        model = models.ValueSet_Filter
        fields = {
            "op": ["exact", "in"],
        }


class ValueSet_Expansion(filters.FilterSet):
    class Meta:
        model = models.ValueSet_Expansion
        fields = {
            "timestamp": ["exact", "gte", "lte"],
            "total": ["exact", "gte", "lte"],
            "offset": ["exact", "gte", "lte"],
        }


class ValueSet_Parameter(filters.FilterSet):
    class Meta:
        model = models.ValueSet_Parameter
        fields = {
            "valueInteger": ["exact", "gte", "lte"],
            "valueDecimal": ["exact", "gte", "lte"],
        }


class ValueSet_Contains(filters.FilterSet):
    class Meta:
        model = models.ValueSet_Contains
        fields = []


class VerificationResult(filters.FilterSet):
    class Meta:
        model = models.VerificationResult
        fields = {
            "statusDate": ["exact", "gte", "lte"],
            "lastPerformed": ["exact", "gte", "lte"],
            "nextScheduled": ["exact", "gte", "lte"],
        }


class VerificationResult_PrimarySource(filters.FilterSet):
    class Meta:
        model = models.VerificationResult_PrimarySource
        fields = {
            "validationDate": ["exact", "gte", "lte"],
        }


class VerificationResult_Attestation(filters.FilterSet):
    class Meta:
        model = models.VerificationResult_Attestation
        fields = {
            "date": ["exact", "gte", "lte"],
        }


class VerificationResult_Validator(filters.FilterSet):
    class Meta:
        model = models.VerificationResult_Validator
        fields = []


class VisionPrescription(filters.FilterSet):
    class Meta:
        model = models.VisionPrescription
        fields = {
            "created": ["exact", "gte", "lte"],
            "dateWritten": ["exact", "gte", "lte"],
        }


class VisionPrescription_LensSpecification(filters.FilterSet):
    class Meta:
        model = models.VisionPrescription_LensSpecification
        fields = {
            "eye": ["exact", "in"],
            "sphere": ["exact", "gte", "lte"],
            "cylinder": ["exact", "gte", "lte"],
            "axis": ["exact", "gte", "lte"],
            "add": ["exact", "gte", "lte"],
            "power": ["exact", "gte", "lte"],
            "backCurve": ["exact", "gte", "lte"],
            "diameter": ["exact", "gte", "lte"],
        }


class VisionPrescription_Prism(filters.FilterSet):
    class Meta:
        model = models.VisionPrescription_Prism
        fields = {
            "amount": ["exact", "gte", "lte"],
            "base": ["exact", "in"],
        }
