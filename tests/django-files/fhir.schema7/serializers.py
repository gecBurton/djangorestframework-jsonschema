from . import models
from rest_framework.serializers import ModelSerializer


class Element(ModelSerializer):
    class Meta:
        model = models.Element
        fields = "__all__"


class Extension(ModelSerializer):
    class Meta:
        model = models.Extension
        fields = "__all__"


class Narrative(ModelSerializer):
    class Meta:
        model = models.Narrative
        fields = "__all__"


class Annotation(ModelSerializer):
    class Meta:
        model = models.Annotation
        fields = "__all__"


class Attachment(ModelSerializer):
    class Meta:
        model = models.Attachment
        fields = "__all__"


class Identifier(ModelSerializer):
    class Meta:
        model = models.Identifier
        fields = "__all__"


class CodeableConcept(ModelSerializer):
    class Meta:
        model = models.CodeableConcept
        fields = "__all__"


class Coding(ModelSerializer):
    class Meta:
        model = models.Coding
        fields = "__all__"


class Quantity(ModelSerializer):
    class Meta:
        model = models.Quantity
        fields = "__all__"


class Duration(ModelSerializer):
    class Meta:
        model = models.Duration
        fields = "__all__"


class Distance(ModelSerializer):
    class Meta:
        model = models.Distance
        fields = "__all__"


class Count(ModelSerializer):
    class Meta:
        model = models.Count
        fields = "__all__"


class Money(ModelSerializer):
    class Meta:
        model = models.Money
        fields = "__all__"


class Age(ModelSerializer):
    class Meta:
        model = models.Age
        fields = "__all__"


class Range(ModelSerializer):
    class Meta:
        model = models.Range
        fields = "__all__"


class Period(ModelSerializer):
    class Meta:
        model = models.Period
        fields = "__all__"


class Ratio(ModelSerializer):
    class Meta:
        model = models.Ratio
        fields = "__all__"


class Reference(ModelSerializer):
    class Meta:
        model = models.Reference
        fields = "__all__"


class SampledData(ModelSerializer):
    class Meta:
        model = models.SampledData
        fields = "__all__"


class Signature(ModelSerializer):
    class Meta:
        model = models.Signature
        fields = "__all__"


class HumanName(ModelSerializer):
    class Meta:
        model = models.HumanName
        fields = "__all__"


class Address(ModelSerializer):
    class Meta:
        model = models.Address
        fields = "__all__"


class ContactPoint(ModelSerializer):
    class Meta:
        model = models.ContactPoint
        fields = "__all__"


class Timing(ModelSerializer):
    class Meta:
        model = models.Timing
        fields = "__all__"


class Timing_Repeat(ModelSerializer):
    class Meta:
        model = models.Timing_Repeat
        fields = "__all__"


class Meta(ModelSerializer):
    class Meta:
        model = models.Meta
        fields = "__all__"


class ContactDetail(ModelSerializer):
    class Meta:
        model = models.ContactDetail
        fields = "__all__"


class Contributor(ModelSerializer):
    class Meta:
        model = models.Contributor
        fields = "__all__"


class DataRequirement(ModelSerializer):
    class Meta:
        model = models.DataRequirement
        fields = "__all__"


class DataRequirement_CodeFilter(ModelSerializer):
    class Meta:
        model = models.DataRequirement_CodeFilter
        fields = "__all__"


class DataRequirement_DateFilter(ModelSerializer):
    class Meta:
        model = models.DataRequirement_DateFilter
        fields = "__all__"


class DataRequirement_Sort(ModelSerializer):
    class Meta:
        model = models.DataRequirement_Sort
        fields = "__all__"


class ParameterDefinition(ModelSerializer):
    class Meta:
        model = models.ParameterDefinition
        fields = "__all__"


class RelatedArtifact(ModelSerializer):
    class Meta:
        model = models.RelatedArtifact
        fields = "__all__"


class TriggerDefinition(ModelSerializer):
    class Meta:
        model = models.TriggerDefinition
        fields = "__all__"


class UsageContext(ModelSerializer):
    class Meta:
        model = models.UsageContext
        fields = "__all__"


class Dosage(ModelSerializer):
    class Meta:
        model = models.Dosage
        fields = "__all__"


class Dosage_DoseAndRate(ModelSerializer):
    class Meta:
        model = models.Dosage_DoseAndRate
        fields = "__all__"


class Population(ModelSerializer):
    class Meta:
        model = models.Population
        fields = "__all__"


class ProductShelfLife(ModelSerializer):
    class Meta:
        model = models.ProductShelfLife
        fields = "__all__"


class ProdCharacteristic(ModelSerializer):
    class Meta:
        model = models.ProdCharacteristic
        fields = "__all__"


class MarketingStatus(ModelSerializer):
    class Meta:
        model = models.MarketingStatus
        fields = "__all__"


class SubstanceAmount(ModelSerializer):
    class Meta:
        model = models.SubstanceAmount
        fields = "__all__"


class SubstanceAmount_ReferenceRange(ModelSerializer):
    class Meta:
        model = models.SubstanceAmount_ReferenceRange
        fields = "__all__"


class Expression(ModelSerializer):
    class Meta:
        model = models.Expression
        fields = "__all__"


class ElementDefinition(ModelSerializer):
    class Meta:
        model = models.ElementDefinition
        fields = "__all__"


class ElementDefinition_Slicing(ModelSerializer):
    class Meta:
        model = models.ElementDefinition_Slicing
        fields = "__all__"


class ElementDefinition_Discriminator(ModelSerializer):
    class Meta:
        model = models.ElementDefinition_Discriminator
        fields = "__all__"


class ElementDefinition_Base(ModelSerializer):
    class Meta:
        model = models.ElementDefinition_Base
        fields = "__all__"


class ElementDefinition_Type(ModelSerializer):
    class Meta:
        model = models.ElementDefinition_Type
        fields = "__all__"


class ElementDefinition_Example(ModelSerializer):
    class Meta:
        model = models.ElementDefinition_Example
        fields = "__all__"


class ElementDefinition_Constraint(ModelSerializer):
    class Meta:
        model = models.ElementDefinition_Constraint
        fields = "__all__"


class ElementDefinition_Binding(ModelSerializer):
    class Meta:
        model = models.ElementDefinition_Binding
        fields = "__all__"


class ElementDefinition_Mapping(ModelSerializer):
    class Meta:
        model = models.ElementDefinition_Mapping
        fields = "__all__"


class Account(ModelSerializer):
    class Meta:
        model = models.Account
        fields = "__all__"


class Account_Coverage(ModelSerializer):
    class Meta:
        model = models.Account_Coverage
        fields = "__all__"


class Account_Guarantor(ModelSerializer):
    class Meta:
        model = models.Account_Guarantor
        fields = "__all__"


class ActivityDefinition(ModelSerializer):
    class Meta:
        model = models.ActivityDefinition
        fields = "__all__"


class ActivityDefinition_Participant(ModelSerializer):
    class Meta:
        model = models.ActivityDefinition_Participant
        fields = "__all__"


class ActivityDefinition_DynamicValue(ModelSerializer):
    class Meta:
        model = models.ActivityDefinition_DynamicValue
        fields = "__all__"


class AdverseEvent(ModelSerializer):
    class Meta:
        model = models.AdverseEvent
        fields = "__all__"


class AdverseEvent_SuspectEntity(ModelSerializer):
    class Meta:
        model = models.AdverseEvent_SuspectEntity
        fields = "__all__"


class AdverseEvent_Causality(ModelSerializer):
    class Meta:
        model = models.AdverseEvent_Causality
        fields = "__all__"


class AllergyIntolerance(ModelSerializer):
    class Meta:
        model = models.AllergyIntolerance
        fields = "__all__"


class AllergyIntolerance_Reaction(ModelSerializer):
    class Meta:
        model = models.AllergyIntolerance_Reaction
        fields = "__all__"


class Appointment(ModelSerializer):
    class Meta:
        model = models.Appointment
        fields = "__all__"


class Appointment_Participant(ModelSerializer):
    class Meta:
        model = models.Appointment_Participant
        fields = "__all__"


class AppointmentResponse(ModelSerializer):
    class Meta:
        model = models.AppointmentResponse
        fields = "__all__"


class AuditEvent(ModelSerializer):
    class Meta:
        model = models.AuditEvent
        fields = "__all__"


class AuditEvent_Agent(ModelSerializer):
    class Meta:
        model = models.AuditEvent_Agent
        fields = "__all__"


class AuditEvent_Network(ModelSerializer):
    class Meta:
        model = models.AuditEvent_Network
        fields = "__all__"


class AuditEvent_Source(ModelSerializer):
    class Meta:
        model = models.AuditEvent_Source
        fields = "__all__"


class AuditEvent_Entity(ModelSerializer):
    class Meta:
        model = models.AuditEvent_Entity
        fields = "__all__"


class AuditEvent_Detail(ModelSerializer):
    class Meta:
        model = models.AuditEvent_Detail
        fields = "__all__"


class Basic(ModelSerializer):
    class Meta:
        model = models.Basic
        fields = "__all__"


class Binary(ModelSerializer):
    class Meta:
        model = models.Binary
        fields = "__all__"


class BiologicallyDerivedProduct(ModelSerializer):
    class Meta:
        model = models.BiologicallyDerivedProduct
        fields = "__all__"


class BiologicallyDerivedProduct_Collection(ModelSerializer):
    class Meta:
        model = models.BiologicallyDerivedProduct_Collection
        fields = "__all__"


class BiologicallyDerivedProduct_Processing(ModelSerializer):
    class Meta:
        model = models.BiologicallyDerivedProduct_Processing
        fields = "__all__"


class BiologicallyDerivedProduct_Manipulation(ModelSerializer):
    class Meta:
        model = models.BiologicallyDerivedProduct_Manipulation
        fields = "__all__"


class BiologicallyDerivedProduct_Storage(ModelSerializer):
    class Meta:
        model = models.BiologicallyDerivedProduct_Storage
        fields = "__all__"


class BodyStructure(ModelSerializer):
    class Meta:
        model = models.BodyStructure
        fields = "__all__"


class Bundle(ModelSerializer):
    class Meta:
        model = models.Bundle
        fields = "__all__"


class Bundle_Link(ModelSerializer):
    class Meta:
        model = models.Bundle_Link
        fields = "__all__"


class Bundle_Entry(ModelSerializer):
    class Meta:
        model = models.Bundle_Entry
        fields = "__all__"


class Bundle_Search(ModelSerializer):
    class Meta:
        model = models.Bundle_Search
        fields = "__all__"


class Bundle_Request(ModelSerializer):
    class Meta:
        model = models.Bundle_Request
        fields = "__all__"


class Bundle_Response(ModelSerializer):
    class Meta:
        model = models.Bundle_Response
        fields = "__all__"


class CapabilityStatement(ModelSerializer):
    class Meta:
        model = models.CapabilityStatement
        fields = "__all__"


class CapabilityStatement_Software(ModelSerializer):
    class Meta:
        model = models.CapabilityStatement_Software
        fields = "__all__"


class CapabilityStatement_Implementation(ModelSerializer):
    class Meta:
        model = models.CapabilityStatement_Implementation
        fields = "__all__"


class CapabilityStatement_Rest(ModelSerializer):
    class Meta:
        model = models.CapabilityStatement_Rest
        fields = "__all__"


class CapabilityStatement_Security(ModelSerializer):
    class Meta:
        model = models.CapabilityStatement_Security
        fields = "__all__"


class CapabilityStatement_Resource(ModelSerializer):
    class Meta:
        model = models.CapabilityStatement_Resource
        fields = "__all__"


class CapabilityStatement_Interaction(ModelSerializer):
    class Meta:
        model = models.CapabilityStatement_Interaction
        fields = "__all__"


class CapabilityStatement_SearchParam(ModelSerializer):
    class Meta:
        model = models.CapabilityStatement_SearchParam
        fields = "__all__"


class CapabilityStatement_Operation(ModelSerializer):
    class Meta:
        model = models.CapabilityStatement_Operation
        fields = "__all__"


class CapabilityStatement_Interaction1(ModelSerializer):
    class Meta:
        model = models.CapabilityStatement_Interaction1
        fields = "__all__"


class CapabilityStatement_Messaging(ModelSerializer):
    class Meta:
        model = models.CapabilityStatement_Messaging
        fields = "__all__"


class CapabilityStatement_Endpoint(ModelSerializer):
    class Meta:
        model = models.CapabilityStatement_Endpoint
        fields = "__all__"


class CapabilityStatement_SupportedMessage(ModelSerializer):
    class Meta:
        model = models.CapabilityStatement_SupportedMessage
        fields = "__all__"


class CapabilityStatement_Document(ModelSerializer):
    class Meta:
        model = models.CapabilityStatement_Document
        fields = "__all__"


class CarePlan(ModelSerializer):
    class Meta:
        model = models.CarePlan
        fields = "__all__"


class CarePlan_Activity(ModelSerializer):
    class Meta:
        model = models.CarePlan_Activity
        fields = "__all__"


class CarePlan_Detail(ModelSerializer):
    class Meta:
        model = models.CarePlan_Detail
        fields = "__all__"


class CareTeam(ModelSerializer):
    class Meta:
        model = models.CareTeam
        fields = "__all__"


class CareTeam_Participant(ModelSerializer):
    class Meta:
        model = models.CareTeam_Participant
        fields = "__all__"


class CatalogEntry(ModelSerializer):
    class Meta:
        model = models.CatalogEntry
        fields = "__all__"


class CatalogEntry_RelatedEntry(ModelSerializer):
    class Meta:
        model = models.CatalogEntry_RelatedEntry
        fields = "__all__"


class ChargeItem(ModelSerializer):
    class Meta:
        model = models.ChargeItem
        fields = "__all__"


class ChargeItem_Performer(ModelSerializer):
    class Meta:
        model = models.ChargeItem_Performer
        fields = "__all__"


class ChargeItemDefinition(ModelSerializer):
    class Meta:
        model = models.ChargeItemDefinition
        fields = "__all__"


class ChargeItemDefinition_Applicability(ModelSerializer):
    class Meta:
        model = models.ChargeItemDefinition_Applicability
        fields = "__all__"


class ChargeItemDefinition_PropertyGroup(ModelSerializer):
    class Meta:
        model = models.ChargeItemDefinition_PropertyGroup
        fields = "__all__"


class ChargeItemDefinition_PriceComponent(ModelSerializer):
    class Meta:
        model = models.ChargeItemDefinition_PriceComponent
        fields = "__all__"


class Claim(ModelSerializer):
    class Meta:
        model = models.Claim
        fields = "__all__"


class Claim_Related(ModelSerializer):
    class Meta:
        model = models.Claim_Related
        fields = "__all__"


class Claim_Payee(ModelSerializer):
    class Meta:
        model = models.Claim_Payee
        fields = "__all__"


class Claim_CareTeam(ModelSerializer):
    class Meta:
        model = models.Claim_CareTeam
        fields = "__all__"


class Claim_SupportingInfo(ModelSerializer):
    class Meta:
        model = models.Claim_SupportingInfo
        fields = "__all__"


class Claim_Diagnosis(ModelSerializer):
    class Meta:
        model = models.Claim_Diagnosis
        fields = "__all__"


class Claim_Procedure(ModelSerializer):
    class Meta:
        model = models.Claim_Procedure
        fields = "__all__"


class Claim_Insurance(ModelSerializer):
    class Meta:
        model = models.Claim_Insurance
        fields = "__all__"


class Claim_Accident(ModelSerializer):
    class Meta:
        model = models.Claim_Accident
        fields = "__all__"


class Claim_Item(ModelSerializer):
    class Meta:
        model = models.Claim_Item
        fields = "__all__"


class Claim_Detail(ModelSerializer):
    class Meta:
        model = models.Claim_Detail
        fields = "__all__"


class Claim_SubDetail(ModelSerializer):
    class Meta:
        model = models.Claim_SubDetail
        fields = "__all__"


class ClaimResponse(ModelSerializer):
    class Meta:
        model = models.ClaimResponse
        fields = "__all__"


class ClaimResponse_Item(ModelSerializer):
    class Meta:
        model = models.ClaimResponse_Item
        fields = "__all__"


class ClaimResponse_Adjudication(ModelSerializer):
    class Meta:
        model = models.ClaimResponse_Adjudication
        fields = "__all__"


class ClaimResponse_Detail(ModelSerializer):
    class Meta:
        model = models.ClaimResponse_Detail
        fields = "__all__"


class ClaimResponse_SubDetail(ModelSerializer):
    class Meta:
        model = models.ClaimResponse_SubDetail
        fields = "__all__"


class ClaimResponse_AddItem(ModelSerializer):
    class Meta:
        model = models.ClaimResponse_AddItem
        fields = "__all__"


class ClaimResponse_Detail1(ModelSerializer):
    class Meta:
        model = models.ClaimResponse_Detail1
        fields = "__all__"


class ClaimResponse_SubDetail1(ModelSerializer):
    class Meta:
        model = models.ClaimResponse_SubDetail1
        fields = "__all__"


class ClaimResponse_Total(ModelSerializer):
    class Meta:
        model = models.ClaimResponse_Total
        fields = "__all__"


class ClaimResponse_Payment(ModelSerializer):
    class Meta:
        model = models.ClaimResponse_Payment
        fields = "__all__"


class ClaimResponse_ProcessNote(ModelSerializer):
    class Meta:
        model = models.ClaimResponse_ProcessNote
        fields = "__all__"


class ClaimResponse_Insurance(ModelSerializer):
    class Meta:
        model = models.ClaimResponse_Insurance
        fields = "__all__"


class ClaimResponse_Error(ModelSerializer):
    class Meta:
        model = models.ClaimResponse_Error
        fields = "__all__"


class ClinicalImpression(ModelSerializer):
    class Meta:
        model = models.ClinicalImpression
        fields = "__all__"


class ClinicalImpression_Investigation(ModelSerializer):
    class Meta:
        model = models.ClinicalImpression_Investigation
        fields = "__all__"


class ClinicalImpression_Finding(ModelSerializer):
    class Meta:
        model = models.ClinicalImpression_Finding
        fields = "__all__"


class CodeSystem(ModelSerializer):
    class Meta:
        model = models.CodeSystem
        fields = "__all__"


class CodeSystem_Filter(ModelSerializer):
    class Meta:
        model = models.CodeSystem_Filter
        fields = "__all__"


class CodeSystem_Property(ModelSerializer):
    class Meta:
        model = models.CodeSystem_Property
        fields = "__all__"


class CodeSystem_Concept(ModelSerializer):
    class Meta:
        model = models.CodeSystem_Concept
        fields = "__all__"


class CodeSystem_Designation(ModelSerializer):
    class Meta:
        model = models.CodeSystem_Designation
        fields = "__all__"


class CodeSystem_Property1(ModelSerializer):
    class Meta:
        model = models.CodeSystem_Property1
        fields = "__all__"


class Communication(ModelSerializer):
    class Meta:
        model = models.Communication
        fields = "__all__"


class Communication_Payload(ModelSerializer):
    class Meta:
        model = models.Communication_Payload
        fields = "__all__"


class CommunicationRequest(ModelSerializer):
    class Meta:
        model = models.CommunicationRequest
        fields = "__all__"


class CommunicationRequest_Payload(ModelSerializer):
    class Meta:
        model = models.CommunicationRequest_Payload
        fields = "__all__"


class CompartmentDefinition(ModelSerializer):
    class Meta:
        model = models.CompartmentDefinition
        fields = "__all__"


class CompartmentDefinition_Resource(ModelSerializer):
    class Meta:
        model = models.CompartmentDefinition_Resource
        fields = "__all__"


class Composition(ModelSerializer):
    class Meta:
        model = models.Composition
        fields = "__all__"


class Composition_Attester(ModelSerializer):
    class Meta:
        model = models.Composition_Attester
        fields = "__all__"


class Composition_RelatesTo(ModelSerializer):
    class Meta:
        model = models.Composition_RelatesTo
        fields = "__all__"


class Composition_Event(ModelSerializer):
    class Meta:
        model = models.Composition_Event
        fields = "__all__"


class Composition_Section(ModelSerializer):
    class Meta:
        model = models.Composition_Section
        fields = "__all__"


class ConceptMap(ModelSerializer):
    class Meta:
        model = models.ConceptMap
        fields = "__all__"


class ConceptMap_Group(ModelSerializer):
    class Meta:
        model = models.ConceptMap_Group
        fields = "__all__"


class ConceptMap_Element(ModelSerializer):
    class Meta:
        model = models.ConceptMap_Element
        fields = "__all__"


class ConceptMap_Target(ModelSerializer):
    class Meta:
        model = models.ConceptMap_Target
        fields = "__all__"


class ConceptMap_DependsOn(ModelSerializer):
    class Meta:
        model = models.ConceptMap_DependsOn
        fields = "__all__"


class ConceptMap_Unmapped(ModelSerializer):
    class Meta:
        model = models.ConceptMap_Unmapped
        fields = "__all__"


class Condition(ModelSerializer):
    class Meta:
        model = models.Condition
        fields = "__all__"


class Condition_Stage(ModelSerializer):
    class Meta:
        model = models.Condition_Stage
        fields = "__all__"


class Condition_Evidence(ModelSerializer):
    class Meta:
        model = models.Condition_Evidence
        fields = "__all__"


class Consent(ModelSerializer):
    class Meta:
        model = models.Consent
        fields = "__all__"


class Consent_Policy(ModelSerializer):
    class Meta:
        model = models.Consent_Policy
        fields = "__all__"


class Consent_Verification(ModelSerializer):
    class Meta:
        model = models.Consent_Verification
        fields = "__all__"


class Consent_Provision(ModelSerializer):
    class Meta:
        model = models.Consent_Provision
        fields = "__all__"


class Consent_Actor(ModelSerializer):
    class Meta:
        model = models.Consent_Actor
        fields = "__all__"


class Consent_Data(ModelSerializer):
    class Meta:
        model = models.Consent_Data
        fields = "__all__"


class Contract(ModelSerializer):
    class Meta:
        model = models.Contract
        fields = "__all__"


class Contract_ContentDefinition(ModelSerializer):
    class Meta:
        model = models.Contract_ContentDefinition
        fields = "__all__"


class Contract_Term(ModelSerializer):
    class Meta:
        model = models.Contract_Term
        fields = "__all__"


class Contract_SecurityLabel(ModelSerializer):
    class Meta:
        model = models.Contract_SecurityLabel
        fields = "__all__"


class Contract_Offer(ModelSerializer):
    class Meta:
        model = models.Contract_Offer
        fields = "__all__"


class Contract_Party(ModelSerializer):
    class Meta:
        model = models.Contract_Party
        fields = "__all__"


class Contract_Answer(ModelSerializer):
    class Meta:
        model = models.Contract_Answer
        fields = "__all__"


class Contract_Asset(ModelSerializer):
    class Meta:
        model = models.Contract_Asset
        fields = "__all__"


class Contract_Context(ModelSerializer):
    class Meta:
        model = models.Contract_Context
        fields = "__all__"


class Contract_ValuedItem(ModelSerializer):
    class Meta:
        model = models.Contract_ValuedItem
        fields = "__all__"


class Contract_Action(ModelSerializer):
    class Meta:
        model = models.Contract_Action
        fields = "__all__"


class Contract_Subject(ModelSerializer):
    class Meta:
        model = models.Contract_Subject
        fields = "__all__"


class Contract_Signer(ModelSerializer):
    class Meta:
        model = models.Contract_Signer
        fields = "__all__"


class Contract_Friendly(ModelSerializer):
    class Meta:
        model = models.Contract_Friendly
        fields = "__all__"


class Contract_Legal(ModelSerializer):
    class Meta:
        model = models.Contract_Legal
        fields = "__all__"


class Contract_Rule(ModelSerializer):
    class Meta:
        model = models.Contract_Rule
        fields = "__all__"


class Coverage(ModelSerializer):
    class Meta:
        model = models.Coverage
        fields = "__all__"


class Coverage_Class(ModelSerializer):
    class Meta:
        model = models.Coverage_Class
        fields = "__all__"


class Coverage_CostToBeneficiary(ModelSerializer):
    class Meta:
        model = models.Coverage_CostToBeneficiary
        fields = "__all__"


class Coverage_Exception(ModelSerializer):
    class Meta:
        model = models.Coverage_Exception
        fields = "__all__"


class CoverageEligibilityRequest(ModelSerializer):
    class Meta:
        model = models.CoverageEligibilityRequest
        fields = "__all__"


class CoverageEligibilityRequest_SupportingInfo(ModelSerializer):
    class Meta:
        model = models.CoverageEligibilityRequest_SupportingInfo
        fields = "__all__"


class CoverageEligibilityRequest_Insurance(ModelSerializer):
    class Meta:
        model = models.CoverageEligibilityRequest_Insurance
        fields = "__all__"


class CoverageEligibilityRequest_Item(ModelSerializer):
    class Meta:
        model = models.CoverageEligibilityRequest_Item
        fields = "__all__"


class CoverageEligibilityRequest_Diagnosis(ModelSerializer):
    class Meta:
        model = models.CoverageEligibilityRequest_Diagnosis
        fields = "__all__"


class CoverageEligibilityResponse(ModelSerializer):
    class Meta:
        model = models.CoverageEligibilityResponse
        fields = "__all__"


class CoverageEligibilityResponse_Insurance(ModelSerializer):
    class Meta:
        model = models.CoverageEligibilityResponse_Insurance
        fields = "__all__"


class CoverageEligibilityResponse_Item(ModelSerializer):
    class Meta:
        model = models.CoverageEligibilityResponse_Item
        fields = "__all__"


class CoverageEligibilityResponse_Benefit(ModelSerializer):
    class Meta:
        model = models.CoverageEligibilityResponse_Benefit
        fields = "__all__"


class CoverageEligibilityResponse_Error(ModelSerializer):
    class Meta:
        model = models.CoverageEligibilityResponse_Error
        fields = "__all__"


class DetectedIssue(ModelSerializer):
    class Meta:
        model = models.DetectedIssue
        fields = "__all__"


class DetectedIssue_Evidence(ModelSerializer):
    class Meta:
        model = models.DetectedIssue_Evidence
        fields = "__all__"


class DetectedIssue_Mitigation(ModelSerializer):
    class Meta:
        model = models.DetectedIssue_Mitigation
        fields = "__all__"


class Device(ModelSerializer):
    class Meta:
        model = models.Device
        fields = "__all__"


class Device_UdiCarrier(ModelSerializer):
    class Meta:
        model = models.Device_UdiCarrier
        fields = "__all__"


class Device_DeviceName(ModelSerializer):
    class Meta:
        model = models.Device_DeviceName
        fields = "__all__"


class Device_Specialization(ModelSerializer):
    class Meta:
        model = models.Device_Specialization
        fields = "__all__"


class Device_Version(ModelSerializer):
    class Meta:
        model = models.Device_Version
        fields = "__all__"


class Device_Property(ModelSerializer):
    class Meta:
        model = models.Device_Property
        fields = "__all__"


class DeviceDefinition(ModelSerializer):
    class Meta:
        model = models.DeviceDefinition
        fields = "__all__"


class DeviceDefinition_UdiDeviceIdentifier(ModelSerializer):
    class Meta:
        model = models.DeviceDefinition_UdiDeviceIdentifier
        fields = "__all__"


class DeviceDefinition_DeviceName(ModelSerializer):
    class Meta:
        model = models.DeviceDefinition_DeviceName
        fields = "__all__"


class DeviceDefinition_Specialization(ModelSerializer):
    class Meta:
        model = models.DeviceDefinition_Specialization
        fields = "__all__"


class DeviceDefinition_Capability(ModelSerializer):
    class Meta:
        model = models.DeviceDefinition_Capability
        fields = "__all__"


class DeviceDefinition_Property(ModelSerializer):
    class Meta:
        model = models.DeviceDefinition_Property
        fields = "__all__"


class DeviceDefinition_Material(ModelSerializer):
    class Meta:
        model = models.DeviceDefinition_Material
        fields = "__all__"


class DeviceMetric(ModelSerializer):
    class Meta:
        model = models.DeviceMetric
        fields = "__all__"


class DeviceMetric_Calibration(ModelSerializer):
    class Meta:
        model = models.DeviceMetric_Calibration
        fields = "__all__"


class DeviceRequest(ModelSerializer):
    class Meta:
        model = models.DeviceRequest
        fields = "__all__"


class DeviceRequest_Parameter(ModelSerializer):
    class Meta:
        model = models.DeviceRequest_Parameter
        fields = "__all__"


class DeviceUseStatement(ModelSerializer):
    class Meta:
        model = models.DeviceUseStatement
        fields = "__all__"


class DiagnosticReport(ModelSerializer):
    class Meta:
        model = models.DiagnosticReport
        fields = "__all__"


class DiagnosticReport_Media(ModelSerializer):
    class Meta:
        model = models.DiagnosticReport_Media
        fields = "__all__"


class DocumentManifest(ModelSerializer):
    class Meta:
        model = models.DocumentManifest
        fields = "__all__"


class DocumentManifest_Related(ModelSerializer):
    class Meta:
        model = models.DocumentManifest_Related
        fields = "__all__"


class DocumentReference(ModelSerializer):
    class Meta:
        model = models.DocumentReference
        fields = "__all__"


class DocumentReference_RelatesTo(ModelSerializer):
    class Meta:
        model = models.DocumentReference_RelatesTo
        fields = "__all__"


class DocumentReference_Content(ModelSerializer):
    class Meta:
        model = models.DocumentReference_Content
        fields = "__all__"


class DocumentReference_Context(ModelSerializer):
    class Meta:
        model = models.DocumentReference_Context
        fields = "__all__"


class EffectEvidenceSynthesis(ModelSerializer):
    class Meta:
        model = models.EffectEvidenceSynthesis
        fields = "__all__"


class EffectEvidenceSynthesis_SampleSize(ModelSerializer):
    class Meta:
        model = models.EffectEvidenceSynthesis_SampleSize
        fields = "__all__"


class EffectEvidenceSynthesis_ResultsByExposure(ModelSerializer):
    class Meta:
        model = models.EffectEvidenceSynthesis_ResultsByExposure
        fields = "__all__"


class EffectEvidenceSynthesis_EffectEstimate(ModelSerializer):
    class Meta:
        model = models.EffectEvidenceSynthesis_EffectEstimate
        fields = "__all__"


class EffectEvidenceSynthesis_PrecisionEstimate(ModelSerializer):
    class Meta:
        model = models.EffectEvidenceSynthesis_PrecisionEstimate
        fields = "__all__"


class EffectEvidenceSynthesis_Certainty(ModelSerializer):
    class Meta:
        model = models.EffectEvidenceSynthesis_Certainty
        fields = "__all__"


class EffectEvidenceSynthesis_CertaintySubcomponent(ModelSerializer):
    class Meta:
        model = models.EffectEvidenceSynthesis_CertaintySubcomponent
        fields = "__all__"


class Encounter(ModelSerializer):
    class Meta:
        model = models.Encounter
        fields = "__all__"


class Encounter_StatusHistory(ModelSerializer):
    class Meta:
        model = models.Encounter_StatusHistory
        fields = "__all__"


class Encounter_ClassHistory(ModelSerializer):
    class Meta:
        model = models.Encounter_ClassHistory
        fields = "__all__"


class Encounter_Participant(ModelSerializer):
    class Meta:
        model = models.Encounter_Participant
        fields = "__all__"


class Encounter_Diagnosis(ModelSerializer):
    class Meta:
        model = models.Encounter_Diagnosis
        fields = "__all__"


class Encounter_Hospitalization(ModelSerializer):
    class Meta:
        model = models.Encounter_Hospitalization
        fields = "__all__"


class Encounter_Location(ModelSerializer):
    class Meta:
        model = models.Encounter_Location
        fields = "__all__"


class Endpoint(ModelSerializer):
    class Meta:
        model = models.Endpoint
        fields = "__all__"


class EnrollmentRequest(ModelSerializer):
    class Meta:
        model = models.EnrollmentRequest
        fields = "__all__"


class EnrollmentResponse(ModelSerializer):
    class Meta:
        model = models.EnrollmentResponse
        fields = "__all__"


class EpisodeOfCare(ModelSerializer):
    class Meta:
        model = models.EpisodeOfCare
        fields = "__all__"


class EpisodeOfCare_StatusHistory(ModelSerializer):
    class Meta:
        model = models.EpisodeOfCare_StatusHistory
        fields = "__all__"


class EpisodeOfCare_Diagnosis(ModelSerializer):
    class Meta:
        model = models.EpisodeOfCare_Diagnosis
        fields = "__all__"


class EventDefinition(ModelSerializer):
    class Meta:
        model = models.EventDefinition
        fields = "__all__"


class Evidence(ModelSerializer):
    class Meta:
        model = models.Evidence
        fields = "__all__"


class EvidenceVariable(ModelSerializer):
    class Meta:
        model = models.EvidenceVariable
        fields = "__all__"


class EvidenceVariable_Characteristic(ModelSerializer):
    class Meta:
        model = models.EvidenceVariable_Characteristic
        fields = "__all__"


class ExampleScenario(ModelSerializer):
    class Meta:
        model = models.ExampleScenario
        fields = "__all__"


class ExampleScenario_Actor(ModelSerializer):
    class Meta:
        model = models.ExampleScenario_Actor
        fields = "__all__"


class ExampleScenario_Instance(ModelSerializer):
    class Meta:
        model = models.ExampleScenario_Instance
        fields = "__all__"


class ExampleScenario_Version(ModelSerializer):
    class Meta:
        model = models.ExampleScenario_Version
        fields = "__all__"


class ExampleScenario_ContainedInstance(ModelSerializer):
    class Meta:
        model = models.ExampleScenario_ContainedInstance
        fields = "__all__"


class ExampleScenario_Process(ModelSerializer):
    class Meta:
        model = models.ExampleScenario_Process
        fields = "__all__"


class ExampleScenario_Step(ModelSerializer):
    class Meta:
        model = models.ExampleScenario_Step
        fields = "__all__"


class ExampleScenario_Operation(ModelSerializer):
    class Meta:
        model = models.ExampleScenario_Operation
        fields = "__all__"


class ExampleScenario_Alternative(ModelSerializer):
    class Meta:
        model = models.ExampleScenario_Alternative
        fields = "__all__"


class ExplanationOfBenefit(ModelSerializer):
    class Meta:
        model = models.ExplanationOfBenefit
        fields = "__all__"


class ExplanationOfBenefit_Related(ModelSerializer):
    class Meta:
        model = models.ExplanationOfBenefit_Related
        fields = "__all__"


class ExplanationOfBenefit_Payee(ModelSerializer):
    class Meta:
        model = models.ExplanationOfBenefit_Payee
        fields = "__all__"


class ExplanationOfBenefit_CareTeam(ModelSerializer):
    class Meta:
        model = models.ExplanationOfBenefit_CareTeam
        fields = "__all__"


class ExplanationOfBenefit_SupportingInfo(ModelSerializer):
    class Meta:
        model = models.ExplanationOfBenefit_SupportingInfo
        fields = "__all__"


class ExplanationOfBenefit_Diagnosis(ModelSerializer):
    class Meta:
        model = models.ExplanationOfBenefit_Diagnosis
        fields = "__all__"


class ExplanationOfBenefit_Procedure(ModelSerializer):
    class Meta:
        model = models.ExplanationOfBenefit_Procedure
        fields = "__all__"


class ExplanationOfBenefit_Insurance(ModelSerializer):
    class Meta:
        model = models.ExplanationOfBenefit_Insurance
        fields = "__all__"


class ExplanationOfBenefit_Accident(ModelSerializer):
    class Meta:
        model = models.ExplanationOfBenefit_Accident
        fields = "__all__"


class ExplanationOfBenefit_Item(ModelSerializer):
    class Meta:
        model = models.ExplanationOfBenefit_Item
        fields = "__all__"


class ExplanationOfBenefit_Adjudication(ModelSerializer):
    class Meta:
        model = models.ExplanationOfBenefit_Adjudication
        fields = "__all__"


class ExplanationOfBenefit_Detail(ModelSerializer):
    class Meta:
        model = models.ExplanationOfBenefit_Detail
        fields = "__all__"


class ExplanationOfBenefit_SubDetail(ModelSerializer):
    class Meta:
        model = models.ExplanationOfBenefit_SubDetail
        fields = "__all__"


class ExplanationOfBenefit_AddItem(ModelSerializer):
    class Meta:
        model = models.ExplanationOfBenefit_AddItem
        fields = "__all__"


class ExplanationOfBenefit_Detail1(ModelSerializer):
    class Meta:
        model = models.ExplanationOfBenefit_Detail1
        fields = "__all__"


class ExplanationOfBenefit_SubDetail1(ModelSerializer):
    class Meta:
        model = models.ExplanationOfBenefit_SubDetail1
        fields = "__all__"


class ExplanationOfBenefit_Total(ModelSerializer):
    class Meta:
        model = models.ExplanationOfBenefit_Total
        fields = "__all__"


class ExplanationOfBenefit_Payment(ModelSerializer):
    class Meta:
        model = models.ExplanationOfBenefit_Payment
        fields = "__all__"


class ExplanationOfBenefit_ProcessNote(ModelSerializer):
    class Meta:
        model = models.ExplanationOfBenefit_ProcessNote
        fields = "__all__"


class ExplanationOfBenefit_BenefitBalance(ModelSerializer):
    class Meta:
        model = models.ExplanationOfBenefit_BenefitBalance
        fields = "__all__"


class ExplanationOfBenefit_Financial(ModelSerializer):
    class Meta:
        model = models.ExplanationOfBenefit_Financial
        fields = "__all__"


class FamilyMemberHistory(ModelSerializer):
    class Meta:
        model = models.FamilyMemberHistory
        fields = "__all__"


class FamilyMemberHistory_Condition(ModelSerializer):
    class Meta:
        model = models.FamilyMemberHistory_Condition
        fields = "__all__"


class Flag(ModelSerializer):
    class Meta:
        model = models.Flag
        fields = "__all__"


class Goal(ModelSerializer):
    class Meta:
        model = models.Goal
        fields = "__all__"


class Goal_Target(ModelSerializer):
    class Meta:
        model = models.Goal_Target
        fields = "__all__"


class GraphDefinition(ModelSerializer):
    class Meta:
        model = models.GraphDefinition
        fields = "__all__"


class GraphDefinition_Link(ModelSerializer):
    class Meta:
        model = models.GraphDefinition_Link
        fields = "__all__"


class GraphDefinition_Target(ModelSerializer):
    class Meta:
        model = models.GraphDefinition_Target
        fields = "__all__"


class GraphDefinition_Compartment(ModelSerializer):
    class Meta:
        model = models.GraphDefinition_Compartment
        fields = "__all__"


class Group(ModelSerializer):
    class Meta:
        model = models.Group
        fields = "__all__"


class Group_Characteristic(ModelSerializer):
    class Meta:
        model = models.Group_Characteristic
        fields = "__all__"


class Group_Member(ModelSerializer):
    class Meta:
        model = models.Group_Member
        fields = "__all__"


class GuidanceResponse(ModelSerializer):
    class Meta:
        model = models.GuidanceResponse
        fields = "__all__"


class HealthcareService(ModelSerializer):
    class Meta:
        model = models.HealthcareService
        fields = "__all__"


class HealthcareService_Eligibility(ModelSerializer):
    class Meta:
        model = models.HealthcareService_Eligibility
        fields = "__all__"


class HealthcareService_AvailableTime(ModelSerializer):
    class Meta:
        model = models.HealthcareService_AvailableTime
        fields = "__all__"


class HealthcareService_NotAvailable(ModelSerializer):
    class Meta:
        model = models.HealthcareService_NotAvailable
        fields = "__all__"


class ImagingStudy(ModelSerializer):
    class Meta:
        model = models.ImagingStudy
        fields = "__all__"


class ImagingStudy_Series(ModelSerializer):
    class Meta:
        model = models.ImagingStudy_Series
        fields = "__all__"


class ImagingStudy_Performer(ModelSerializer):
    class Meta:
        model = models.ImagingStudy_Performer
        fields = "__all__"


class ImagingStudy_Instance(ModelSerializer):
    class Meta:
        model = models.ImagingStudy_Instance
        fields = "__all__"


class Immunization(ModelSerializer):
    class Meta:
        model = models.Immunization
        fields = "__all__"


class Immunization_Performer(ModelSerializer):
    class Meta:
        model = models.Immunization_Performer
        fields = "__all__"


class Immunization_Education(ModelSerializer):
    class Meta:
        model = models.Immunization_Education
        fields = "__all__"


class Immunization_Reaction(ModelSerializer):
    class Meta:
        model = models.Immunization_Reaction
        fields = "__all__"


class Immunization_ProtocolApplied(ModelSerializer):
    class Meta:
        model = models.Immunization_ProtocolApplied
        fields = "__all__"


class ImmunizationEvaluation(ModelSerializer):
    class Meta:
        model = models.ImmunizationEvaluation
        fields = "__all__"


class ImmunizationRecommendation(ModelSerializer):
    class Meta:
        model = models.ImmunizationRecommendation
        fields = "__all__"


class ImmunizationRecommendation_Recommendation(ModelSerializer):
    class Meta:
        model = models.ImmunizationRecommendation_Recommendation
        fields = "__all__"


class ImmunizationRecommendation_DateCriterion(ModelSerializer):
    class Meta:
        model = models.ImmunizationRecommendation_DateCriterion
        fields = "__all__"


class ImplementationGuide(ModelSerializer):
    class Meta:
        model = models.ImplementationGuide
        fields = "__all__"


class ImplementationGuide_DependsOn(ModelSerializer):
    class Meta:
        model = models.ImplementationGuide_DependsOn
        fields = "__all__"


class ImplementationGuide_Global(ModelSerializer):
    class Meta:
        model = models.ImplementationGuide_Global
        fields = "__all__"


class ImplementationGuide_Definition(ModelSerializer):
    class Meta:
        model = models.ImplementationGuide_Definition
        fields = "__all__"


class ImplementationGuide_Grouping(ModelSerializer):
    class Meta:
        model = models.ImplementationGuide_Grouping
        fields = "__all__"


class ImplementationGuide_Resource(ModelSerializer):
    class Meta:
        model = models.ImplementationGuide_Resource
        fields = "__all__"


class ImplementationGuide_Page(ModelSerializer):
    class Meta:
        model = models.ImplementationGuide_Page
        fields = "__all__"


class ImplementationGuide_Parameter(ModelSerializer):
    class Meta:
        model = models.ImplementationGuide_Parameter
        fields = "__all__"


class ImplementationGuide_Template(ModelSerializer):
    class Meta:
        model = models.ImplementationGuide_Template
        fields = "__all__"


class ImplementationGuide_Manifest(ModelSerializer):
    class Meta:
        model = models.ImplementationGuide_Manifest
        fields = "__all__"


class ImplementationGuide_Resource1(ModelSerializer):
    class Meta:
        model = models.ImplementationGuide_Resource1
        fields = "__all__"


class ImplementationGuide_Page1(ModelSerializer):
    class Meta:
        model = models.ImplementationGuide_Page1
        fields = "__all__"


class InsurancePlan(ModelSerializer):
    class Meta:
        model = models.InsurancePlan
        fields = "__all__"


class InsurancePlan_Contact(ModelSerializer):
    class Meta:
        model = models.InsurancePlan_Contact
        fields = "__all__"


class InsurancePlan_Coverage(ModelSerializer):
    class Meta:
        model = models.InsurancePlan_Coverage
        fields = "__all__"


class InsurancePlan_Benefit(ModelSerializer):
    class Meta:
        model = models.InsurancePlan_Benefit
        fields = "__all__"


class InsurancePlan_Limit(ModelSerializer):
    class Meta:
        model = models.InsurancePlan_Limit
        fields = "__all__"


class InsurancePlan_Plan(ModelSerializer):
    class Meta:
        model = models.InsurancePlan_Plan
        fields = "__all__"


class InsurancePlan_GeneralCost(ModelSerializer):
    class Meta:
        model = models.InsurancePlan_GeneralCost
        fields = "__all__"


class InsurancePlan_SpecificCost(ModelSerializer):
    class Meta:
        model = models.InsurancePlan_SpecificCost
        fields = "__all__"


class InsurancePlan_Benefit1(ModelSerializer):
    class Meta:
        model = models.InsurancePlan_Benefit1
        fields = "__all__"


class InsurancePlan_Cost(ModelSerializer):
    class Meta:
        model = models.InsurancePlan_Cost
        fields = "__all__"


class Invoice(ModelSerializer):
    class Meta:
        model = models.Invoice
        fields = "__all__"


class Invoice_Participant(ModelSerializer):
    class Meta:
        model = models.Invoice_Participant
        fields = "__all__"


class Invoice_LineItem(ModelSerializer):
    class Meta:
        model = models.Invoice_LineItem
        fields = "__all__"


class Invoice_PriceComponent(ModelSerializer):
    class Meta:
        model = models.Invoice_PriceComponent
        fields = "__all__"


class Library(ModelSerializer):
    class Meta:
        model = models.Library
        fields = "__all__"


class Linkage(ModelSerializer):
    class Meta:
        model = models.Linkage
        fields = "__all__"


class Linkage_Item(ModelSerializer):
    class Meta:
        model = models.Linkage_Item
        fields = "__all__"


class List(ModelSerializer):
    class Meta:
        model = models.List
        fields = "__all__"


class List_Entry(ModelSerializer):
    class Meta:
        model = models.List_Entry
        fields = "__all__"


class Location(ModelSerializer):
    class Meta:
        model = models.Location
        fields = "__all__"


class Location_Position(ModelSerializer):
    class Meta:
        model = models.Location_Position
        fields = "__all__"


class Location_HoursOfOperation(ModelSerializer):
    class Meta:
        model = models.Location_HoursOfOperation
        fields = "__all__"


class Measure(ModelSerializer):
    class Meta:
        model = models.Measure
        fields = "__all__"


class Measure_Group(ModelSerializer):
    class Meta:
        model = models.Measure_Group
        fields = "__all__"


class Measure_Population(ModelSerializer):
    class Meta:
        model = models.Measure_Population
        fields = "__all__"


class Measure_Stratifier(ModelSerializer):
    class Meta:
        model = models.Measure_Stratifier
        fields = "__all__"


class Measure_Component(ModelSerializer):
    class Meta:
        model = models.Measure_Component
        fields = "__all__"


class Measure_SupplementalData(ModelSerializer):
    class Meta:
        model = models.Measure_SupplementalData
        fields = "__all__"


class MeasureReport(ModelSerializer):
    class Meta:
        model = models.MeasureReport
        fields = "__all__"


class MeasureReport_Group(ModelSerializer):
    class Meta:
        model = models.MeasureReport_Group
        fields = "__all__"


class MeasureReport_Population(ModelSerializer):
    class Meta:
        model = models.MeasureReport_Population
        fields = "__all__"


class MeasureReport_Stratifier(ModelSerializer):
    class Meta:
        model = models.MeasureReport_Stratifier
        fields = "__all__"


class MeasureReport_Stratum(ModelSerializer):
    class Meta:
        model = models.MeasureReport_Stratum
        fields = "__all__"


class MeasureReport_Component(ModelSerializer):
    class Meta:
        model = models.MeasureReport_Component
        fields = "__all__"


class MeasureReport_Population1(ModelSerializer):
    class Meta:
        model = models.MeasureReport_Population1
        fields = "__all__"


class Media(ModelSerializer):
    class Meta:
        model = models.Media
        fields = "__all__"


class Medication(ModelSerializer):
    class Meta:
        model = models.Medication
        fields = "__all__"


class Medication_Ingredient(ModelSerializer):
    class Meta:
        model = models.Medication_Ingredient
        fields = "__all__"


class Medication_Batch(ModelSerializer):
    class Meta:
        model = models.Medication_Batch
        fields = "__all__"


class MedicationAdministration(ModelSerializer):
    class Meta:
        model = models.MedicationAdministration
        fields = "__all__"


class MedicationAdministration_Performer(ModelSerializer):
    class Meta:
        model = models.MedicationAdministration_Performer
        fields = "__all__"


class MedicationAdministration_Dosage(ModelSerializer):
    class Meta:
        model = models.MedicationAdministration_Dosage
        fields = "__all__"


class MedicationDispense(ModelSerializer):
    class Meta:
        model = models.MedicationDispense
        fields = "__all__"


class MedicationDispense_Performer(ModelSerializer):
    class Meta:
        model = models.MedicationDispense_Performer
        fields = "__all__"


class MedicationDispense_Substitution(ModelSerializer):
    class Meta:
        model = models.MedicationDispense_Substitution
        fields = "__all__"


class MedicationKnowledge(ModelSerializer):
    class Meta:
        model = models.MedicationKnowledge
        fields = "__all__"


class MedicationKnowledge_RelatedMedicationKnowledge(ModelSerializer):
    class Meta:
        model = models.MedicationKnowledge_RelatedMedicationKnowledge
        fields = "__all__"


class MedicationKnowledge_Monograph(ModelSerializer):
    class Meta:
        model = models.MedicationKnowledge_Monograph
        fields = "__all__"


class MedicationKnowledge_Ingredient(ModelSerializer):
    class Meta:
        model = models.MedicationKnowledge_Ingredient
        fields = "__all__"


class MedicationKnowledge_Cost(ModelSerializer):
    class Meta:
        model = models.MedicationKnowledge_Cost
        fields = "__all__"


class MedicationKnowledge_MonitoringProgram(ModelSerializer):
    class Meta:
        model = models.MedicationKnowledge_MonitoringProgram
        fields = "__all__"


class MedicationKnowledge_AdministrationGuidelines(ModelSerializer):
    class Meta:
        model = models.MedicationKnowledge_AdministrationGuidelines
        fields = "__all__"


class MedicationKnowledge_Dosage(ModelSerializer):
    class Meta:
        model = models.MedicationKnowledge_Dosage
        fields = "__all__"


class MedicationKnowledge_PatientCharacteristics(ModelSerializer):
    class Meta:
        model = models.MedicationKnowledge_PatientCharacteristics
        fields = "__all__"


class MedicationKnowledge_MedicineClassification(ModelSerializer):
    class Meta:
        model = models.MedicationKnowledge_MedicineClassification
        fields = "__all__"


class MedicationKnowledge_Packaging(ModelSerializer):
    class Meta:
        model = models.MedicationKnowledge_Packaging
        fields = "__all__"


class MedicationKnowledge_DrugCharacteristic(ModelSerializer):
    class Meta:
        model = models.MedicationKnowledge_DrugCharacteristic
        fields = "__all__"


class MedicationKnowledge_Regulatory(ModelSerializer):
    class Meta:
        model = models.MedicationKnowledge_Regulatory
        fields = "__all__"


class MedicationKnowledge_Substitution(ModelSerializer):
    class Meta:
        model = models.MedicationKnowledge_Substitution
        fields = "__all__"


class MedicationKnowledge_Schedule(ModelSerializer):
    class Meta:
        model = models.MedicationKnowledge_Schedule
        fields = "__all__"


class MedicationKnowledge_MaxDispense(ModelSerializer):
    class Meta:
        model = models.MedicationKnowledge_MaxDispense
        fields = "__all__"


class MedicationKnowledge_Kinetics(ModelSerializer):
    class Meta:
        model = models.MedicationKnowledge_Kinetics
        fields = "__all__"


class MedicationRequest(ModelSerializer):
    class Meta:
        model = models.MedicationRequest
        fields = "__all__"


class MedicationRequest_DispenseRequest(ModelSerializer):
    class Meta:
        model = models.MedicationRequest_DispenseRequest
        fields = "__all__"


class MedicationRequest_InitialFill(ModelSerializer):
    class Meta:
        model = models.MedicationRequest_InitialFill
        fields = "__all__"


class MedicationRequest_Substitution(ModelSerializer):
    class Meta:
        model = models.MedicationRequest_Substitution
        fields = "__all__"


class MedicationStatement(ModelSerializer):
    class Meta:
        model = models.MedicationStatement
        fields = "__all__"


class MedicinalProduct(ModelSerializer):
    class Meta:
        model = models.MedicinalProduct
        fields = "__all__"


class MedicinalProduct_Name(ModelSerializer):
    class Meta:
        model = models.MedicinalProduct_Name
        fields = "__all__"


class MedicinalProduct_NamePart(ModelSerializer):
    class Meta:
        model = models.MedicinalProduct_NamePart
        fields = "__all__"


class MedicinalProduct_CountryLanguage(ModelSerializer):
    class Meta:
        model = models.MedicinalProduct_CountryLanguage
        fields = "__all__"


class MedicinalProduct_ManufacturingBusinessOperation(ModelSerializer):
    class Meta:
        model = models.MedicinalProduct_ManufacturingBusinessOperation
        fields = "__all__"


class MedicinalProduct_SpecialDesignation(ModelSerializer):
    class Meta:
        model = models.MedicinalProduct_SpecialDesignation
        fields = "__all__"


class MedicinalProductAuthorization(ModelSerializer):
    class Meta:
        model = models.MedicinalProductAuthorization
        fields = "__all__"


class MedicinalProductAuthorization_JurisdictionalAuthorization(ModelSerializer):
    class Meta:
        model = models.MedicinalProductAuthorization_JurisdictionalAuthorization
        fields = "__all__"


class MedicinalProductAuthorization_Procedure(ModelSerializer):
    class Meta:
        model = models.MedicinalProductAuthorization_Procedure
        fields = "__all__"


class MedicinalProductContraindication(ModelSerializer):
    class Meta:
        model = models.MedicinalProductContraindication
        fields = "__all__"


class MedicinalProductContraindication_OtherTherapy(ModelSerializer):
    class Meta:
        model = models.MedicinalProductContraindication_OtherTherapy
        fields = "__all__"


class MedicinalProductIndication(ModelSerializer):
    class Meta:
        model = models.MedicinalProductIndication
        fields = "__all__"


class MedicinalProductIndication_OtherTherapy(ModelSerializer):
    class Meta:
        model = models.MedicinalProductIndication_OtherTherapy
        fields = "__all__"


class MedicinalProductIngredient(ModelSerializer):
    class Meta:
        model = models.MedicinalProductIngredient
        fields = "__all__"


class MedicinalProductIngredient_SpecifiedSubstance(ModelSerializer):
    class Meta:
        model = models.MedicinalProductIngredient_SpecifiedSubstance
        fields = "__all__"


class MedicinalProductIngredient_Strength(ModelSerializer):
    class Meta:
        model = models.MedicinalProductIngredient_Strength
        fields = "__all__"


class MedicinalProductIngredient_ReferenceStrength(ModelSerializer):
    class Meta:
        model = models.MedicinalProductIngredient_ReferenceStrength
        fields = "__all__"


class MedicinalProductIngredient_Substance(ModelSerializer):
    class Meta:
        model = models.MedicinalProductIngredient_Substance
        fields = "__all__"


class MedicinalProductInteraction(ModelSerializer):
    class Meta:
        model = models.MedicinalProductInteraction
        fields = "__all__"


class MedicinalProductInteraction_Interactant(ModelSerializer):
    class Meta:
        model = models.MedicinalProductInteraction_Interactant
        fields = "__all__"


class MedicinalProductManufactured(ModelSerializer):
    class Meta:
        model = models.MedicinalProductManufactured
        fields = "__all__"


class MedicinalProductPackaged(ModelSerializer):
    class Meta:
        model = models.MedicinalProductPackaged
        fields = "__all__"


class MedicinalProductPackaged_BatchIdentifier(ModelSerializer):
    class Meta:
        model = models.MedicinalProductPackaged_BatchIdentifier
        fields = "__all__"


class MedicinalProductPackaged_PackageItem(ModelSerializer):
    class Meta:
        model = models.MedicinalProductPackaged_PackageItem
        fields = "__all__"


class MedicinalProductPharmaceutical(ModelSerializer):
    class Meta:
        model = models.MedicinalProductPharmaceutical
        fields = "__all__"


class MedicinalProductPharmaceutical_Characteristics(ModelSerializer):
    class Meta:
        model = models.MedicinalProductPharmaceutical_Characteristics
        fields = "__all__"


class MedicinalProductPharmaceutical_RouteOfAdministration(ModelSerializer):
    class Meta:
        model = models.MedicinalProductPharmaceutical_RouteOfAdministration
        fields = "__all__"


class MedicinalProductPharmaceutical_TargetSpecies(ModelSerializer):
    class Meta:
        model = models.MedicinalProductPharmaceutical_TargetSpecies
        fields = "__all__"


class MedicinalProductPharmaceutical_WithdrawalPeriod(ModelSerializer):
    class Meta:
        model = models.MedicinalProductPharmaceutical_WithdrawalPeriod
        fields = "__all__"


class MedicinalProductUndesirableEffect(ModelSerializer):
    class Meta:
        model = models.MedicinalProductUndesirableEffect
        fields = "__all__"


class MessageDefinition(ModelSerializer):
    class Meta:
        model = models.MessageDefinition
        fields = "__all__"


class MessageDefinition_Focus(ModelSerializer):
    class Meta:
        model = models.MessageDefinition_Focus
        fields = "__all__"


class MessageDefinition_AllowedResponse(ModelSerializer):
    class Meta:
        model = models.MessageDefinition_AllowedResponse
        fields = "__all__"


class MessageHeader(ModelSerializer):
    class Meta:
        model = models.MessageHeader
        fields = "__all__"


class MessageHeader_Destination(ModelSerializer):
    class Meta:
        model = models.MessageHeader_Destination
        fields = "__all__"


class MessageHeader_Source(ModelSerializer):
    class Meta:
        model = models.MessageHeader_Source
        fields = "__all__"


class MessageHeader_Response(ModelSerializer):
    class Meta:
        model = models.MessageHeader_Response
        fields = "__all__"


class MolecularSequence(ModelSerializer):
    class Meta:
        model = models.MolecularSequence
        fields = "__all__"


class MolecularSequence_ReferenceSeq(ModelSerializer):
    class Meta:
        model = models.MolecularSequence_ReferenceSeq
        fields = "__all__"


class MolecularSequence_Variant(ModelSerializer):
    class Meta:
        model = models.MolecularSequence_Variant
        fields = "__all__"


class MolecularSequence_Quality(ModelSerializer):
    class Meta:
        model = models.MolecularSequence_Quality
        fields = "__all__"


class MolecularSequence_Roc(ModelSerializer):
    class Meta:
        model = models.MolecularSequence_Roc
        fields = "__all__"


class MolecularSequence_Repository(ModelSerializer):
    class Meta:
        model = models.MolecularSequence_Repository
        fields = "__all__"


class MolecularSequence_StructureVariant(ModelSerializer):
    class Meta:
        model = models.MolecularSequence_StructureVariant
        fields = "__all__"


class MolecularSequence_Outer(ModelSerializer):
    class Meta:
        model = models.MolecularSequence_Outer
        fields = "__all__"


class MolecularSequence_Inner(ModelSerializer):
    class Meta:
        model = models.MolecularSequence_Inner
        fields = "__all__"


class NamingSystem(ModelSerializer):
    class Meta:
        model = models.NamingSystem
        fields = "__all__"


class NamingSystem_UniqueId(ModelSerializer):
    class Meta:
        model = models.NamingSystem_UniqueId
        fields = "__all__"


class NutritionOrder(ModelSerializer):
    class Meta:
        model = models.NutritionOrder
        fields = "__all__"


class NutritionOrder_OralDiet(ModelSerializer):
    class Meta:
        model = models.NutritionOrder_OralDiet
        fields = "__all__"


class NutritionOrder_Nutrient(ModelSerializer):
    class Meta:
        model = models.NutritionOrder_Nutrient
        fields = "__all__"


class NutritionOrder_Texture(ModelSerializer):
    class Meta:
        model = models.NutritionOrder_Texture
        fields = "__all__"


class NutritionOrder_Supplement(ModelSerializer):
    class Meta:
        model = models.NutritionOrder_Supplement
        fields = "__all__"


class NutritionOrder_EnteralFormula(ModelSerializer):
    class Meta:
        model = models.NutritionOrder_EnteralFormula
        fields = "__all__"


class NutritionOrder_Administration(ModelSerializer):
    class Meta:
        model = models.NutritionOrder_Administration
        fields = "__all__"


class Observation(ModelSerializer):
    class Meta:
        model = models.Observation
        fields = "__all__"


class Observation_ReferenceRange(ModelSerializer):
    class Meta:
        model = models.Observation_ReferenceRange
        fields = "__all__"


class Observation_Component(ModelSerializer):
    class Meta:
        model = models.Observation_Component
        fields = "__all__"


class ObservationDefinition(ModelSerializer):
    class Meta:
        model = models.ObservationDefinition
        fields = "__all__"


class ObservationDefinition_QuantitativeDetails(ModelSerializer):
    class Meta:
        model = models.ObservationDefinition_QuantitativeDetails
        fields = "__all__"


class ObservationDefinition_QualifiedInterval(ModelSerializer):
    class Meta:
        model = models.ObservationDefinition_QualifiedInterval
        fields = "__all__"


class OperationDefinition(ModelSerializer):
    class Meta:
        model = models.OperationDefinition
        fields = "__all__"


class OperationDefinition_Parameter(ModelSerializer):
    class Meta:
        model = models.OperationDefinition_Parameter
        fields = "__all__"


class OperationDefinition_Binding(ModelSerializer):
    class Meta:
        model = models.OperationDefinition_Binding
        fields = "__all__"


class OperationDefinition_ReferencedFrom(ModelSerializer):
    class Meta:
        model = models.OperationDefinition_ReferencedFrom
        fields = "__all__"


class OperationDefinition_Overload(ModelSerializer):
    class Meta:
        model = models.OperationDefinition_Overload
        fields = "__all__"


class OperationOutcome(ModelSerializer):
    class Meta:
        model = models.OperationOutcome
        fields = "__all__"


class OperationOutcome_Issue(ModelSerializer):
    class Meta:
        model = models.OperationOutcome_Issue
        fields = "__all__"


class Organization(ModelSerializer):
    class Meta:
        model = models.Organization
        fields = "__all__"


class Organization_Contact(ModelSerializer):
    class Meta:
        model = models.Organization_Contact
        fields = "__all__"


class OrganizationAffiliation(ModelSerializer):
    class Meta:
        model = models.OrganizationAffiliation
        fields = "__all__"


class Parameters(ModelSerializer):
    class Meta:
        model = models.Parameters
        fields = "__all__"


class Parameters_Parameter(ModelSerializer):
    class Meta:
        model = models.Parameters_Parameter
        fields = "__all__"


class Patient(ModelSerializer):
    class Meta:
        model = models.Patient
        fields = "__all__"


class Patient_Contact(ModelSerializer):
    class Meta:
        model = models.Patient_Contact
        fields = "__all__"


class Patient_Communication(ModelSerializer):
    class Meta:
        model = models.Patient_Communication
        fields = "__all__"


class Patient_Link(ModelSerializer):
    class Meta:
        model = models.Patient_Link
        fields = "__all__"


class PaymentNotice(ModelSerializer):
    class Meta:
        model = models.PaymentNotice
        fields = "__all__"


class PaymentReconciliation(ModelSerializer):
    class Meta:
        model = models.PaymentReconciliation
        fields = "__all__"


class PaymentReconciliation_Detail(ModelSerializer):
    class Meta:
        model = models.PaymentReconciliation_Detail
        fields = "__all__"


class PaymentReconciliation_ProcessNote(ModelSerializer):
    class Meta:
        model = models.PaymentReconciliation_ProcessNote
        fields = "__all__"


class Person(ModelSerializer):
    class Meta:
        model = models.Person
        fields = "__all__"


class Person_Link(ModelSerializer):
    class Meta:
        model = models.Person_Link
        fields = "__all__"


class PlanDefinition(ModelSerializer):
    class Meta:
        model = models.PlanDefinition
        fields = "__all__"


class PlanDefinition_Goal(ModelSerializer):
    class Meta:
        model = models.PlanDefinition_Goal
        fields = "__all__"


class PlanDefinition_Target(ModelSerializer):
    class Meta:
        model = models.PlanDefinition_Target
        fields = "__all__"


class PlanDefinition_Action(ModelSerializer):
    class Meta:
        model = models.PlanDefinition_Action
        fields = "__all__"


class PlanDefinition_Condition(ModelSerializer):
    class Meta:
        model = models.PlanDefinition_Condition
        fields = "__all__"


class PlanDefinition_RelatedAction(ModelSerializer):
    class Meta:
        model = models.PlanDefinition_RelatedAction
        fields = "__all__"


class PlanDefinition_Participant(ModelSerializer):
    class Meta:
        model = models.PlanDefinition_Participant
        fields = "__all__"


class PlanDefinition_DynamicValue(ModelSerializer):
    class Meta:
        model = models.PlanDefinition_DynamicValue
        fields = "__all__"


class Practitioner(ModelSerializer):
    class Meta:
        model = models.Practitioner
        fields = "__all__"


class Practitioner_Qualification(ModelSerializer):
    class Meta:
        model = models.Practitioner_Qualification
        fields = "__all__"


class PractitionerRole(ModelSerializer):
    class Meta:
        model = models.PractitionerRole
        fields = "__all__"


class PractitionerRole_AvailableTime(ModelSerializer):
    class Meta:
        model = models.PractitionerRole_AvailableTime
        fields = "__all__"


class PractitionerRole_NotAvailable(ModelSerializer):
    class Meta:
        model = models.PractitionerRole_NotAvailable
        fields = "__all__"


class Procedure(ModelSerializer):
    class Meta:
        model = models.Procedure
        fields = "__all__"


class Procedure_Performer(ModelSerializer):
    class Meta:
        model = models.Procedure_Performer
        fields = "__all__"


class Procedure_FocalDevice(ModelSerializer):
    class Meta:
        model = models.Procedure_FocalDevice
        fields = "__all__"


class Provenance(ModelSerializer):
    class Meta:
        model = models.Provenance
        fields = "__all__"


class Provenance_Agent(ModelSerializer):
    class Meta:
        model = models.Provenance_Agent
        fields = "__all__"


class Provenance_Entity(ModelSerializer):
    class Meta:
        model = models.Provenance_Entity
        fields = "__all__"


class Questionnaire(ModelSerializer):
    class Meta:
        model = models.Questionnaire
        fields = "__all__"


class Questionnaire_Item(ModelSerializer):
    class Meta:
        model = models.Questionnaire_Item
        fields = "__all__"


class Questionnaire_EnableWhen(ModelSerializer):
    class Meta:
        model = models.Questionnaire_EnableWhen
        fields = "__all__"


class Questionnaire_AnswerOption(ModelSerializer):
    class Meta:
        model = models.Questionnaire_AnswerOption
        fields = "__all__"


class Questionnaire_Initial(ModelSerializer):
    class Meta:
        model = models.Questionnaire_Initial
        fields = "__all__"


class QuestionnaireResponse(ModelSerializer):
    class Meta:
        model = models.QuestionnaireResponse
        fields = "__all__"


class QuestionnaireResponse_Item(ModelSerializer):
    class Meta:
        model = models.QuestionnaireResponse_Item
        fields = "__all__"


class QuestionnaireResponse_Answer(ModelSerializer):
    class Meta:
        model = models.QuestionnaireResponse_Answer
        fields = "__all__"


class RelatedPerson(ModelSerializer):
    class Meta:
        model = models.RelatedPerson
        fields = "__all__"


class RelatedPerson_Communication(ModelSerializer):
    class Meta:
        model = models.RelatedPerson_Communication
        fields = "__all__"


class RequestGroup(ModelSerializer):
    class Meta:
        model = models.RequestGroup
        fields = "__all__"


class RequestGroup_Action(ModelSerializer):
    class Meta:
        model = models.RequestGroup_Action
        fields = "__all__"


class RequestGroup_Condition(ModelSerializer):
    class Meta:
        model = models.RequestGroup_Condition
        fields = "__all__"


class RequestGroup_RelatedAction(ModelSerializer):
    class Meta:
        model = models.RequestGroup_RelatedAction
        fields = "__all__"


class ResearchDefinition(ModelSerializer):
    class Meta:
        model = models.ResearchDefinition
        fields = "__all__"


class ResearchElementDefinition(ModelSerializer):
    class Meta:
        model = models.ResearchElementDefinition
        fields = "__all__"


class ResearchElementDefinition_Characteristic(ModelSerializer):
    class Meta:
        model = models.ResearchElementDefinition_Characteristic
        fields = "__all__"


class ResearchStudy(ModelSerializer):
    class Meta:
        model = models.ResearchStudy
        fields = "__all__"


class ResearchStudy_Arm(ModelSerializer):
    class Meta:
        model = models.ResearchStudy_Arm
        fields = "__all__"


class ResearchStudy_Objective(ModelSerializer):
    class Meta:
        model = models.ResearchStudy_Objective
        fields = "__all__"


class ResearchSubject(ModelSerializer):
    class Meta:
        model = models.ResearchSubject
        fields = "__all__"


class RiskAssessment(ModelSerializer):
    class Meta:
        model = models.RiskAssessment
        fields = "__all__"


class RiskAssessment_Prediction(ModelSerializer):
    class Meta:
        model = models.RiskAssessment_Prediction
        fields = "__all__"


class RiskEvidenceSynthesis(ModelSerializer):
    class Meta:
        model = models.RiskEvidenceSynthesis
        fields = "__all__"


class RiskEvidenceSynthesis_SampleSize(ModelSerializer):
    class Meta:
        model = models.RiskEvidenceSynthesis_SampleSize
        fields = "__all__"


class RiskEvidenceSynthesis_RiskEstimate(ModelSerializer):
    class Meta:
        model = models.RiskEvidenceSynthesis_RiskEstimate
        fields = "__all__"


class RiskEvidenceSynthesis_PrecisionEstimate(ModelSerializer):
    class Meta:
        model = models.RiskEvidenceSynthesis_PrecisionEstimate
        fields = "__all__"


class RiskEvidenceSynthesis_Certainty(ModelSerializer):
    class Meta:
        model = models.RiskEvidenceSynthesis_Certainty
        fields = "__all__"


class RiskEvidenceSynthesis_CertaintySubcomponent(ModelSerializer):
    class Meta:
        model = models.RiskEvidenceSynthesis_CertaintySubcomponent
        fields = "__all__"


class Schedule(ModelSerializer):
    class Meta:
        model = models.Schedule
        fields = "__all__"


class SearchParameter(ModelSerializer):
    class Meta:
        model = models.SearchParameter
        fields = "__all__"


class SearchParameter_Component(ModelSerializer):
    class Meta:
        model = models.SearchParameter_Component
        fields = "__all__"


class ServiceRequest(ModelSerializer):
    class Meta:
        model = models.ServiceRequest
        fields = "__all__"


class Slot(ModelSerializer):
    class Meta:
        model = models.Slot
        fields = "__all__"


class Specimen(ModelSerializer):
    class Meta:
        model = models.Specimen
        fields = "__all__"


class Specimen_Collection(ModelSerializer):
    class Meta:
        model = models.Specimen_Collection
        fields = "__all__"


class Specimen_Processing(ModelSerializer):
    class Meta:
        model = models.Specimen_Processing
        fields = "__all__"


class Specimen_Container(ModelSerializer):
    class Meta:
        model = models.Specimen_Container
        fields = "__all__"


class SpecimenDefinition(ModelSerializer):
    class Meta:
        model = models.SpecimenDefinition
        fields = "__all__"


class SpecimenDefinition_TypeTested(ModelSerializer):
    class Meta:
        model = models.SpecimenDefinition_TypeTested
        fields = "__all__"


class SpecimenDefinition_Container(ModelSerializer):
    class Meta:
        model = models.SpecimenDefinition_Container
        fields = "__all__"


class SpecimenDefinition_Additive(ModelSerializer):
    class Meta:
        model = models.SpecimenDefinition_Additive
        fields = "__all__"


class SpecimenDefinition_Handling(ModelSerializer):
    class Meta:
        model = models.SpecimenDefinition_Handling
        fields = "__all__"


class StructureDefinition(ModelSerializer):
    class Meta:
        model = models.StructureDefinition
        fields = "__all__"


class StructureDefinition_Mapping(ModelSerializer):
    class Meta:
        model = models.StructureDefinition_Mapping
        fields = "__all__"


class StructureDefinition_Context(ModelSerializer):
    class Meta:
        model = models.StructureDefinition_Context
        fields = "__all__"


class StructureDefinition_Snapshot(ModelSerializer):
    class Meta:
        model = models.StructureDefinition_Snapshot
        fields = "__all__"


class StructureDefinition_Differential(ModelSerializer):
    class Meta:
        model = models.StructureDefinition_Differential
        fields = "__all__"


class StructureMap(ModelSerializer):
    class Meta:
        model = models.StructureMap
        fields = "__all__"


class StructureMap_Structure(ModelSerializer):
    class Meta:
        model = models.StructureMap_Structure
        fields = "__all__"


class StructureMap_Group(ModelSerializer):
    class Meta:
        model = models.StructureMap_Group
        fields = "__all__"


class StructureMap_Input(ModelSerializer):
    class Meta:
        model = models.StructureMap_Input
        fields = "__all__"


class StructureMap_Rule(ModelSerializer):
    class Meta:
        model = models.StructureMap_Rule
        fields = "__all__"


class StructureMap_Source(ModelSerializer):
    class Meta:
        model = models.StructureMap_Source
        fields = "__all__"


class StructureMap_Target(ModelSerializer):
    class Meta:
        model = models.StructureMap_Target
        fields = "__all__"


class StructureMap_Parameter(ModelSerializer):
    class Meta:
        model = models.StructureMap_Parameter
        fields = "__all__"


class StructureMap_Dependent(ModelSerializer):
    class Meta:
        model = models.StructureMap_Dependent
        fields = "__all__"


class Subscription(ModelSerializer):
    class Meta:
        model = models.Subscription
        fields = "__all__"


class Subscription_Channel(ModelSerializer):
    class Meta:
        model = models.Subscription_Channel
        fields = "__all__"


class Substance(ModelSerializer):
    class Meta:
        model = models.Substance
        fields = "__all__"


class Substance_Instance(ModelSerializer):
    class Meta:
        model = models.Substance_Instance
        fields = "__all__"


class Substance_Ingredient(ModelSerializer):
    class Meta:
        model = models.Substance_Ingredient
        fields = "__all__"


class SubstanceNucleicAcid(ModelSerializer):
    class Meta:
        model = models.SubstanceNucleicAcid
        fields = "__all__"


class SubstanceNucleicAcid_Subunit(ModelSerializer):
    class Meta:
        model = models.SubstanceNucleicAcid_Subunit
        fields = "__all__"


class SubstanceNucleicAcid_Linkage(ModelSerializer):
    class Meta:
        model = models.SubstanceNucleicAcid_Linkage
        fields = "__all__"


class SubstanceNucleicAcid_Sugar(ModelSerializer):
    class Meta:
        model = models.SubstanceNucleicAcid_Sugar
        fields = "__all__"


class SubstancePolymer(ModelSerializer):
    class Meta:
        model = models.SubstancePolymer
        fields = "__all__"


class SubstancePolymer_MonomerSet(ModelSerializer):
    class Meta:
        model = models.SubstancePolymer_MonomerSet
        fields = "__all__"


class SubstancePolymer_StartingMaterial(ModelSerializer):
    class Meta:
        model = models.SubstancePolymer_StartingMaterial
        fields = "__all__"


class SubstancePolymer_Repeat(ModelSerializer):
    class Meta:
        model = models.SubstancePolymer_Repeat
        fields = "__all__"


class SubstancePolymer_RepeatUnit(ModelSerializer):
    class Meta:
        model = models.SubstancePolymer_RepeatUnit
        fields = "__all__"


class SubstancePolymer_DegreeOfPolymerisation(ModelSerializer):
    class Meta:
        model = models.SubstancePolymer_DegreeOfPolymerisation
        fields = "__all__"


class SubstancePolymer_StructuralRepresentation(ModelSerializer):
    class Meta:
        model = models.SubstancePolymer_StructuralRepresentation
        fields = "__all__"


class SubstanceProtein(ModelSerializer):
    class Meta:
        model = models.SubstanceProtein
        fields = "__all__"


class SubstanceProtein_Subunit(ModelSerializer):
    class Meta:
        model = models.SubstanceProtein_Subunit
        fields = "__all__"


class SubstanceReferenceInformation(ModelSerializer):
    class Meta:
        model = models.SubstanceReferenceInformation
        fields = "__all__"


class SubstanceReferenceInformation_Gene(ModelSerializer):
    class Meta:
        model = models.SubstanceReferenceInformation_Gene
        fields = "__all__"


class SubstanceReferenceInformation_GeneElement(ModelSerializer):
    class Meta:
        model = models.SubstanceReferenceInformation_GeneElement
        fields = "__all__"


class SubstanceReferenceInformation_Classification(ModelSerializer):
    class Meta:
        model = models.SubstanceReferenceInformation_Classification
        fields = "__all__"


class SubstanceReferenceInformation_Target(ModelSerializer):
    class Meta:
        model = models.SubstanceReferenceInformation_Target
        fields = "__all__"


class SubstanceSourceMaterial(ModelSerializer):
    class Meta:
        model = models.SubstanceSourceMaterial
        fields = "__all__"


class SubstanceSourceMaterial_FractionDescription(ModelSerializer):
    class Meta:
        model = models.SubstanceSourceMaterial_FractionDescription
        fields = "__all__"


class SubstanceSourceMaterial_Organism(ModelSerializer):
    class Meta:
        model = models.SubstanceSourceMaterial_Organism
        fields = "__all__"


class SubstanceSourceMaterial_Author(ModelSerializer):
    class Meta:
        model = models.SubstanceSourceMaterial_Author
        fields = "__all__"


class SubstanceSourceMaterial_Hybrid(ModelSerializer):
    class Meta:
        model = models.SubstanceSourceMaterial_Hybrid
        fields = "__all__"


class SubstanceSourceMaterial_OrganismGeneral(ModelSerializer):
    class Meta:
        model = models.SubstanceSourceMaterial_OrganismGeneral
        fields = "__all__"


class SubstanceSourceMaterial_PartDescription(ModelSerializer):
    class Meta:
        model = models.SubstanceSourceMaterial_PartDescription
        fields = "__all__"


class SubstanceSpecification(ModelSerializer):
    class Meta:
        model = models.SubstanceSpecification
        fields = "__all__"


class SubstanceSpecification_Moiety(ModelSerializer):
    class Meta:
        model = models.SubstanceSpecification_Moiety
        fields = "__all__"


class SubstanceSpecification_Property(ModelSerializer):
    class Meta:
        model = models.SubstanceSpecification_Property
        fields = "__all__"


class SubstanceSpecification_Structure(ModelSerializer):
    class Meta:
        model = models.SubstanceSpecification_Structure
        fields = "__all__"


class SubstanceSpecification_Isotope(ModelSerializer):
    class Meta:
        model = models.SubstanceSpecification_Isotope
        fields = "__all__"


class SubstanceSpecification_MolecularWeight(ModelSerializer):
    class Meta:
        model = models.SubstanceSpecification_MolecularWeight
        fields = "__all__"


class SubstanceSpecification_Representation(ModelSerializer):
    class Meta:
        model = models.SubstanceSpecification_Representation
        fields = "__all__"


class SubstanceSpecification_Code(ModelSerializer):
    class Meta:
        model = models.SubstanceSpecification_Code
        fields = "__all__"


class SubstanceSpecification_Name(ModelSerializer):
    class Meta:
        model = models.SubstanceSpecification_Name
        fields = "__all__"


class SubstanceSpecification_Official(ModelSerializer):
    class Meta:
        model = models.SubstanceSpecification_Official
        fields = "__all__"


class SubstanceSpecification_Relationship(ModelSerializer):
    class Meta:
        model = models.SubstanceSpecification_Relationship
        fields = "__all__"


class SupplyDelivery(ModelSerializer):
    class Meta:
        model = models.SupplyDelivery
        fields = "__all__"


class SupplyDelivery_SuppliedItem(ModelSerializer):
    class Meta:
        model = models.SupplyDelivery_SuppliedItem
        fields = "__all__"


class SupplyRequest(ModelSerializer):
    class Meta:
        model = models.SupplyRequest
        fields = "__all__"


class SupplyRequest_Parameter(ModelSerializer):
    class Meta:
        model = models.SupplyRequest_Parameter
        fields = "__all__"


class Task(ModelSerializer):
    class Meta:
        model = models.Task
        fields = "__all__"


class Task_Restriction(ModelSerializer):
    class Meta:
        model = models.Task_Restriction
        fields = "__all__"


class Task_Input(ModelSerializer):
    class Meta:
        model = models.Task_Input
        fields = "__all__"


class Task_Output(ModelSerializer):
    class Meta:
        model = models.Task_Output
        fields = "__all__"


class TerminologyCapabilities(ModelSerializer):
    class Meta:
        model = models.TerminologyCapabilities
        fields = "__all__"


class TerminologyCapabilities_Software(ModelSerializer):
    class Meta:
        model = models.TerminologyCapabilities_Software
        fields = "__all__"


class TerminologyCapabilities_Implementation(ModelSerializer):
    class Meta:
        model = models.TerminologyCapabilities_Implementation
        fields = "__all__"


class TerminologyCapabilities_CodeSystem(ModelSerializer):
    class Meta:
        model = models.TerminologyCapabilities_CodeSystem
        fields = "__all__"


class TerminologyCapabilities_Version(ModelSerializer):
    class Meta:
        model = models.TerminologyCapabilities_Version
        fields = "__all__"


class TerminologyCapabilities_Filter(ModelSerializer):
    class Meta:
        model = models.TerminologyCapabilities_Filter
        fields = "__all__"


class TerminologyCapabilities_Expansion(ModelSerializer):
    class Meta:
        model = models.TerminologyCapabilities_Expansion
        fields = "__all__"


class TerminologyCapabilities_Parameter(ModelSerializer):
    class Meta:
        model = models.TerminologyCapabilities_Parameter
        fields = "__all__"


class TerminologyCapabilities_ValidateCode(ModelSerializer):
    class Meta:
        model = models.TerminologyCapabilities_ValidateCode
        fields = "__all__"


class TerminologyCapabilities_Translation(ModelSerializer):
    class Meta:
        model = models.TerminologyCapabilities_Translation
        fields = "__all__"


class TerminologyCapabilities_Closure(ModelSerializer):
    class Meta:
        model = models.TerminologyCapabilities_Closure
        fields = "__all__"


class TestReport(ModelSerializer):
    class Meta:
        model = models.TestReport
        fields = "__all__"


class TestReport_Participant(ModelSerializer):
    class Meta:
        model = models.TestReport_Participant
        fields = "__all__"


class TestReport_Setup(ModelSerializer):
    class Meta:
        model = models.TestReport_Setup
        fields = "__all__"


class TestReport_Action(ModelSerializer):
    class Meta:
        model = models.TestReport_Action
        fields = "__all__"


class TestReport_Operation(ModelSerializer):
    class Meta:
        model = models.TestReport_Operation
        fields = "__all__"


class TestReport_Assert(ModelSerializer):
    class Meta:
        model = models.TestReport_Assert
        fields = "__all__"


class TestReport_Test(ModelSerializer):
    class Meta:
        model = models.TestReport_Test
        fields = "__all__"


class TestReport_Action1(ModelSerializer):
    class Meta:
        model = models.TestReport_Action1
        fields = "__all__"


class TestReport_Teardown(ModelSerializer):
    class Meta:
        model = models.TestReport_Teardown
        fields = "__all__"


class TestReport_Action2(ModelSerializer):
    class Meta:
        model = models.TestReport_Action2
        fields = "__all__"


class TestScript(ModelSerializer):
    class Meta:
        model = models.TestScript
        fields = "__all__"


class TestScript_Origin(ModelSerializer):
    class Meta:
        model = models.TestScript_Origin
        fields = "__all__"


class TestScript_Destination(ModelSerializer):
    class Meta:
        model = models.TestScript_Destination
        fields = "__all__"


class TestScript_Metadata(ModelSerializer):
    class Meta:
        model = models.TestScript_Metadata
        fields = "__all__"


class TestScript_Link(ModelSerializer):
    class Meta:
        model = models.TestScript_Link
        fields = "__all__"


class TestScript_Capability(ModelSerializer):
    class Meta:
        model = models.TestScript_Capability
        fields = "__all__"


class TestScript_Fixture(ModelSerializer):
    class Meta:
        model = models.TestScript_Fixture
        fields = "__all__"


class TestScript_Variable(ModelSerializer):
    class Meta:
        model = models.TestScript_Variable
        fields = "__all__"


class TestScript_Setup(ModelSerializer):
    class Meta:
        model = models.TestScript_Setup
        fields = "__all__"


class TestScript_Action(ModelSerializer):
    class Meta:
        model = models.TestScript_Action
        fields = "__all__"


class TestScript_Operation(ModelSerializer):
    class Meta:
        model = models.TestScript_Operation
        fields = "__all__"


class TestScript_RequestHeader(ModelSerializer):
    class Meta:
        model = models.TestScript_RequestHeader
        fields = "__all__"


class TestScript_Assert(ModelSerializer):
    class Meta:
        model = models.TestScript_Assert
        fields = "__all__"


class TestScript_Test(ModelSerializer):
    class Meta:
        model = models.TestScript_Test
        fields = "__all__"


class TestScript_Action1(ModelSerializer):
    class Meta:
        model = models.TestScript_Action1
        fields = "__all__"


class TestScript_Teardown(ModelSerializer):
    class Meta:
        model = models.TestScript_Teardown
        fields = "__all__"


class TestScript_Action2(ModelSerializer):
    class Meta:
        model = models.TestScript_Action2
        fields = "__all__"


class ValueSet(ModelSerializer):
    class Meta:
        model = models.ValueSet
        fields = "__all__"


class ValueSet_Compose(ModelSerializer):
    class Meta:
        model = models.ValueSet_Compose
        fields = "__all__"


class ValueSet_Include(ModelSerializer):
    class Meta:
        model = models.ValueSet_Include
        fields = "__all__"


class ValueSet_Concept(ModelSerializer):
    class Meta:
        model = models.ValueSet_Concept
        fields = "__all__"


class ValueSet_Designation(ModelSerializer):
    class Meta:
        model = models.ValueSet_Designation
        fields = "__all__"


class ValueSet_Filter(ModelSerializer):
    class Meta:
        model = models.ValueSet_Filter
        fields = "__all__"


class ValueSet_Expansion(ModelSerializer):
    class Meta:
        model = models.ValueSet_Expansion
        fields = "__all__"


class ValueSet_Parameter(ModelSerializer):
    class Meta:
        model = models.ValueSet_Parameter
        fields = "__all__"


class ValueSet_Contains(ModelSerializer):
    class Meta:
        model = models.ValueSet_Contains
        fields = "__all__"


class VerificationResult(ModelSerializer):
    class Meta:
        model = models.VerificationResult
        fields = "__all__"


class VerificationResult_PrimarySource(ModelSerializer):
    class Meta:
        model = models.VerificationResult_PrimarySource
        fields = "__all__"


class VerificationResult_Attestation(ModelSerializer):
    class Meta:
        model = models.VerificationResult_Attestation
        fields = "__all__"


class VerificationResult_Validator(ModelSerializer):
    class Meta:
        model = models.VerificationResult_Validator
        fields = "__all__"


class VisionPrescription(ModelSerializer):
    class Meta:
        model = models.VisionPrescription
        fields = "__all__"


class VisionPrescription_LensSpecification(ModelSerializer):
    class Meta:
        model = models.VisionPrescription_LensSpecification
        fields = "__all__"


class VisionPrescription_Prism(ModelSerializer):
    class Meta:
        model = models.VisionPrescription_Prism
        fields = "__all__"
