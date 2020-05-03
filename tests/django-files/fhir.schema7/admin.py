from django.contrib import admin
from . import models


@admin.register(models.Element)
class ElementAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Extension)
class ExtensionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Narrative)
class NarrativeAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.Annotation)
class AnnotationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Identifier)
class IdentifierAdmin(admin.ModelAdmin):
    list_filter = (
        "use",
    )


@admin.register(models.CodeableConcept)
class CodeableConceptAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Coding)
class CodingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Quantity)
class QuantityAdmin(admin.ModelAdmin):
    list_filter = (
        "comparator",
    )


@admin.register(models.Duration)
class DurationAdmin(admin.ModelAdmin):
    list_filter = (
        "comparator",
    )


@admin.register(models.Distance)
class DistanceAdmin(admin.ModelAdmin):
    list_filter = (
        "comparator",
    )


@admin.register(models.Count)
class CountAdmin(admin.ModelAdmin):
    list_filter = (
        "comparator",
    )


@admin.register(models.Money)
class MoneyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Age)
class AgeAdmin(admin.ModelAdmin):
    list_filter = (
        "comparator",
    )


@admin.register(models.Range)
class RangeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Period)
class PeriodAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Ratio)
class RatioAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Reference)
class ReferenceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SampledData)
class SampledDataAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Signature)
class SignatureAdmin(admin.ModelAdmin):
    pass


@admin.register(models.HumanName)
class HumanNameAdmin(admin.ModelAdmin):
    list_filter = (
        "use",
    )


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_filter = (
        "use",
        "type",
    )


@admin.register(models.ContactPoint)
class ContactPointAdmin(admin.ModelAdmin):
    list_filter = (
        "system",
        "use",
    )


@admin.register(models.Timing)
class TimingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Timing_Repeat)
class Timing_RepeatAdmin(admin.ModelAdmin):
    list_filter = (
        "durationUnit",
        "periodUnit",
    )


@admin.register(models.Meta)
class MetaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ContactDetail)
class ContactDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.DataRequirement)
class DataRequirementAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DataRequirement_CodeFilter)
class DataRequirement_CodeFilterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DataRequirement_DateFilter)
class DataRequirement_DateFilterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DataRequirement_Sort)
class DataRequirement_SortAdmin(admin.ModelAdmin):
    list_filter = (
        "direction",
    )


@admin.register(models.ParameterDefinition)
class ParameterDefinitionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RelatedArtifact)
class RelatedArtifactAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.TriggerDefinition)
class TriggerDefinitionAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.UsageContext)
class UsageContextAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Dosage)
class DosageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Dosage_DoseAndRate)
class Dosage_DoseAndRateAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Population)
class PopulationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ProductShelfLife)
class ProductShelfLifeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ProdCharacteristic)
class ProdCharacteristicAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MarketingStatus)
class MarketingStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceAmount)
class SubstanceAmountAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceAmount_ReferenceRange)
class SubstanceAmount_ReferenceRangeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Expression)
class ExpressionAdmin(admin.ModelAdmin):
    list_filter = (
        "language",
    )


@admin.register(models.ElementDefinition)
class ElementDefinitionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ElementDefinition_Slicing)
class ElementDefinition_SlicingAdmin(admin.ModelAdmin):
    list_filter = (
        "rules",
    )


@admin.register(models.ElementDefinition_Discriminator)
class ElementDefinition_DiscriminatorAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.ElementDefinition_Base)
class ElementDefinition_BaseAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ElementDefinition_Type)
class ElementDefinition_TypeAdmin(admin.ModelAdmin):
    list_filter = (
        "versioning",
    )


@admin.register(models.ElementDefinition_Example)
class ElementDefinition_ExampleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ElementDefinition_Constraint)
class ElementDefinition_ConstraintAdmin(admin.ModelAdmin):
    list_filter = (
        "severity",
    )


@admin.register(models.ElementDefinition_Binding)
class ElementDefinition_BindingAdmin(admin.ModelAdmin):
    list_filter = (
        "strength",
    )


@admin.register(models.ElementDefinition_Mapping)
class ElementDefinition_MappingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.Account_Coverage)
class Account_CoverageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Account_Guarantor)
class Account_GuarantorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ActivityDefinition)
class ActivityDefinitionAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.ActivityDefinition_Participant)
class ActivityDefinition_ParticipantAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ActivityDefinition_DynamicValue)
class ActivityDefinition_DynamicValueAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AdverseEvent)
class AdverseEventAdmin(admin.ModelAdmin):
    list_filter = (
        "actuality",
    )


@admin.register(models.AdverseEvent_SuspectEntity)
class AdverseEvent_SuspectEntityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AdverseEvent_Causality)
class AdverseEvent_CausalityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AllergyIntolerance)
class AllergyIntoleranceAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
        "criticality",
    )


@admin.register(models.AllergyIntolerance_Reaction)
class AllergyIntolerance_ReactionAdmin(admin.ModelAdmin):
    list_filter = (
        "severity",
    )


@admin.register(models.Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.Appointment_Participant)
class Appointment_ParticipantAdmin(admin.ModelAdmin):
    list_filter = (
        "required",
        "status",
    )


@admin.register(models.AppointmentResponse)
class AppointmentResponseAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AuditEvent)
class AuditEventAdmin(admin.ModelAdmin):
    list_filter = (
        "action",
        "outcome",
    )


@admin.register(models.AuditEvent_Agent)
class AuditEvent_AgentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AuditEvent_Network)
class AuditEvent_NetworkAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.AuditEvent_Source)
class AuditEvent_SourceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AuditEvent_Entity)
class AuditEvent_EntityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AuditEvent_Detail)
class AuditEvent_DetailAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Basic)
class BasicAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Binary)
class BinaryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BiologicallyDerivedProduct)
class BiologicallyDerivedProductAdmin(admin.ModelAdmin):
    list_filter = (
        "productCategory",
        "status",
    )


@admin.register(models.BiologicallyDerivedProduct_Collection)
class BiologicallyDerivedProduct_CollectionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BiologicallyDerivedProduct_Processing)
class BiologicallyDerivedProduct_ProcessingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BiologicallyDerivedProduct_Manipulation)
class BiologicallyDerivedProduct_ManipulationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BiologicallyDerivedProduct_Storage)
class BiologicallyDerivedProduct_StorageAdmin(admin.ModelAdmin):
    list_filter = (
        "scale",
    )


@admin.register(models.BodyStructure)
class BodyStructureAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Bundle)
class BundleAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.Bundle_Link)
class Bundle_LinkAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Bundle_Entry)
class Bundle_EntryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Bundle_Search)
class Bundle_SearchAdmin(admin.ModelAdmin):
    list_filter = (
        "mode",
    )


@admin.register(models.Bundle_Request)
class Bundle_RequestAdmin(admin.ModelAdmin):
    list_filter = (
        "method",
    )


@admin.register(models.Bundle_Response)
class Bundle_ResponseAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CapabilityStatement)
class CapabilityStatementAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
        "kind",
        "fhirVersion",
    )


@admin.register(models.CapabilityStatement_Software)
class CapabilityStatement_SoftwareAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CapabilityStatement_Implementation)
class CapabilityStatement_ImplementationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CapabilityStatement_Rest)
class CapabilityStatement_RestAdmin(admin.ModelAdmin):
    list_filter = (
        "mode",
    )


@admin.register(models.CapabilityStatement_Security)
class CapabilityStatement_SecurityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CapabilityStatement_Resource)
class CapabilityStatement_ResourceAdmin(admin.ModelAdmin):
    list_filter = (
        "versioning",
        "conditionalRead",
        "conditionalDelete",
    )


@admin.register(models.CapabilityStatement_Interaction)
class CapabilityStatement_InteractionAdmin(admin.ModelAdmin):
    list_filter = (
        "code",
    )


@admin.register(models.CapabilityStatement_SearchParam)
class CapabilityStatement_SearchParamAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.CapabilityStatement_Operation)
class CapabilityStatement_OperationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CapabilityStatement_Interaction1)
class CapabilityStatement_Interaction1Admin(admin.ModelAdmin):
    list_filter = (
        "code",
    )


@admin.register(models.CapabilityStatement_Messaging)
class CapabilityStatement_MessagingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CapabilityStatement_Endpoint)
class CapabilityStatement_EndpointAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CapabilityStatement_SupportedMessage)
class CapabilityStatement_SupportedMessageAdmin(admin.ModelAdmin):
    list_filter = (
        "mode",
    )


@admin.register(models.CapabilityStatement_Document)
class CapabilityStatement_DocumentAdmin(admin.ModelAdmin):
    list_filter = (
        "mode",
    )


@admin.register(models.CarePlan)
class CarePlanAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CarePlan_Activity)
class CarePlan_ActivityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CarePlan_Detail)
class CarePlan_DetailAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.CareTeam)
class CareTeamAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.CareTeam_Participant)
class CareTeam_ParticipantAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CatalogEntry)
class CatalogEntryAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.CatalogEntry_RelatedEntry)
class CatalogEntry_RelatedEntryAdmin(admin.ModelAdmin):
    list_filter = (
        "relationtype",
    )


@admin.register(models.ChargeItem)
class ChargeItemAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.ChargeItem_Performer)
class ChargeItem_PerformerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ChargeItemDefinition)
class ChargeItemDefinitionAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.ChargeItemDefinition_Applicability)
class ChargeItemDefinition_ApplicabilityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ChargeItemDefinition_PropertyGroup)
class ChargeItemDefinition_PropertyGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ChargeItemDefinition_PriceComponent)
class ChargeItemDefinition_PriceComponentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_filter = (
        "use",
    )


@admin.register(models.Claim_Related)
class Claim_RelatedAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Claim_Payee)
class Claim_PayeeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Claim_CareTeam)
class Claim_CareTeamAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Claim_SupportingInfo)
class Claim_SupportingInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Claim_Diagnosis)
class Claim_DiagnosisAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Claim_Procedure)
class Claim_ProcedureAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Claim_Insurance)
class Claim_InsuranceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Claim_Accident)
class Claim_AccidentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Claim_Item)
class Claim_ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Claim_Detail)
class Claim_DetailAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Claim_SubDetail)
class Claim_SubDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ClaimResponse)
class ClaimResponseAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ClaimResponse_Item)
class ClaimResponse_ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ClaimResponse_Adjudication)
class ClaimResponse_AdjudicationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ClaimResponse_Detail)
class ClaimResponse_DetailAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ClaimResponse_SubDetail)
class ClaimResponse_SubDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ClaimResponse_AddItem)
class ClaimResponse_AddItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ClaimResponse_Detail1)
class ClaimResponse_Detail1Admin(admin.ModelAdmin):
    pass


@admin.register(models.ClaimResponse_SubDetail1)
class ClaimResponse_SubDetail1Admin(admin.ModelAdmin):
    pass


@admin.register(models.ClaimResponse_Total)
class ClaimResponse_TotalAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ClaimResponse_Payment)
class ClaimResponse_PaymentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ClaimResponse_ProcessNote)
class ClaimResponse_ProcessNoteAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.ClaimResponse_Insurance)
class ClaimResponse_InsuranceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ClaimResponse_Error)
class ClaimResponse_ErrorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ClinicalImpression)
class ClinicalImpressionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ClinicalImpression_Investigation)
class ClinicalImpression_InvestigationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ClinicalImpression_Finding)
class ClinicalImpression_FindingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CodeSystem)
class CodeSystemAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
        "hierarchyMeaning",
        "content",
    )


@admin.register(models.CodeSystem_Filter)
class CodeSystem_FilterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CodeSystem_Property)
class CodeSystem_PropertyAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.CodeSystem_Concept)
class CodeSystem_ConceptAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CodeSystem_Designation)
class CodeSystem_DesignationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CodeSystem_Property1)
class CodeSystem_Property1Admin(admin.ModelAdmin):
    pass


@admin.register(models.Communication)
class CommunicationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Communication_Payload)
class Communication_PayloadAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CommunicationRequest)
class CommunicationRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CommunicationRequest_Payload)
class CommunicationRequest_PayloadAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CompartmentDefinition)
class CompartmentDefinitionAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
        "code",
    )


@admin.register(models.CompartmentDefinition_Resource)
class CompartmentDefinition_ResourceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Composition)
class CompositionAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.Composition_Attester)
class Composition_AttesterAdmin(admin.ModelAdmin):
    list_filter = (
        "mode",
    )


@admin.register(models.Composition_RelatesTo)
class Composition_RelatesToAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Composition_Event)
class Composition_EventAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Composition_Section)
class Composition_SectionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ConceptMap)
class ConceptMapAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.ConceptMap_Group)
class ConceptMap_GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ConceptMap_Element)
class ConceptMap_ElementAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ConceptMap_Target)
class ConceptMap_TargetAdmin(admin.ModelAdmin):
    list_filter = (
        "equivalence",
    )


@admin.register(models.ConceptMap_DependsOn)
class ConceptMap_DependsOnAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ConceptMap_Unmapped)
class ConceptMap_UnmappedAdmin(admin.ModelAdmin):
    list_filter = (
        "mode",
    )


@admin.register(models.Condition)
class ConditionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Condition_Stage)
class Condition_StageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Condition_Evidence)
class Condition_EvidenceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Consent)
class ConsentAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.Consent_Policy)
class Consent_PolicyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Consent_Verification)
class Consent_VerificationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Consent_Provision)
class Consent_ProvisionAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.Consent_Actor)
class Consent_ActorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Consent_Data)
class Consent_DataAdmin(admin.ModelAdmin):
    list_filter = (
        "meaning",
    )


@admin.register(models.Contract)
class ContractAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Contract_ContentDefinition)
class Contract_ContentDefinitionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Contract_Term)
class Contract_TermAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Contract_SecurityLabel)
class Contract_SecurityLabelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Contract_Offer)
class Contract_OfferAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Contract_Party)
class Contract_PartyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Contract_Answer)
class Contract_AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Contract_Asset)
class Contract_AssetAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Contract_Context)
class Contract_ContextAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Contract_ValuedItem)
class Contract_ValuedItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Contract_Action)
class Contract_ActionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Contract_Subject)
class Contract_SubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Contract_Signer)
class Contract_SignerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Contract_Friendly)
class Contract_FriendlyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Contract_Legal)
class Contract_LegalAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Contract_Rule)
class Contract_RuleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Coverage)
class CoverageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Coverage_Class)
class Coverage_ClassAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Coverage_CostToBeneficiary)
class Coverage_CostToBeneficiaryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Coverage_Exception)
class Coverage_ExceptionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CoverageEligibilityRequest)
class CoverageEligibilityRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CoverageEligibilityRequest_SupportingInfo)
class CoverageEligibilityRequest_SupportingInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CoverageEligibilityRequest_Insurance)
class CoverageEligibilityRequest_InsuranceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CoverageEligibilityRequest_Item)
class CoverageEligibilityRequest_ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CoverageEligibilityRequest_Diagnosis)
class CoverageEligibilityRequest_DiagnosisAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CoverageEligibilityResponse)
class CoverageEligibilityResponseAdmin(admin.ModelAdmin):
    list_filter = (
        "outcome",
    )


@admin.register(models.CoverageEligibilityResponse_Insurance)
class CoverageEligibilityResponse_InsuranceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CoverageEligibilityResponse_Item)
class CoverageEligibilityResponse_ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CoverageEligibilityResponse_Benefit)
class CoverageEligibilityResponse_BenefitAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CoverageEligibilityResponse_Error)
class CoverageEligibilityResponse_ErrorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DetectedIssue)
class DetectedIssueAdmin(admin.ModelAdmin):
    list_filter = (
        "severity",
    )


@admin.register(models.DetectedIssue_Evidence)
class DetectedIssue_EvidenceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DetectedIssue_Mitigation)
class DetectedIssue_MitigationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Device)
class DeviceAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.Device_UdiCarrier)
class Device_UdiCarrierAdmin(admin.ModelAdmin):
    list_filter = (
        "entryType",
    )


@admin.register(models.Device_DeviceName)
class Device_DeviceNameAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.Device_Specialization)
class Device_SpecializationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Device_Version)
class Device_VersionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Device_Property)
class Device_PropertyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DeviceDefinition)
class DeviceDefinitionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DeviceDefinition_UdiDeviceIdentifier)
class DeviceDefinition_UdiDeviceIdentifierAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DeviceDefinition_DeviceName)
class DeviceDefinition_DeviceNameAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.DeviceDefinition_Specialization)
class DeviceDefinition_SpecializationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DeviceDefinition_Capability)
class DeviceDefinition_CapabilityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DeviceDefinition_Property)
class DeviceDefinition_PropertyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DeviceDefinition_Material)
class DeviceDefinition_MaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DeviceMetric)
class DeviceMetricAdmin(admin.ModelAdmin):
    list_filter = (
        "operationalStatus",
        "color",
        "category",
    )


@admin.register(models.DeviceMetric_Calibration)
class DeviceMetric_CalibrationAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
        "state",
    )


@admin.register(models.DeviceRequest)
class DeviceRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DeviceRequest_Parameter)
class DeviceRequest_ParameterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DeviceUseStatement)
class DeviceUseStatementAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.DiagnosticReport)
class DiagnosticReportAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.DiagnosticReport_Media)
class DiagnosticReport_MediaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DocumentManifest)
class DocumentManifestAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.DocumentManifest_Related)
class DocumentManifest_RelatedAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DocumentReference)
class DocumentReferenceAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.DocumentReference_RelatesTo)
class DocumentReference_RelatesToAdmin(admin.ModelAdmin):
    list_filter = (
        "code",
    )


@admin.register(models.DocumentReference_Content)
class DocumentReference_ContentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DocumentReference_Context)
class DocumentReference_ContextAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EffectEvidenceSynthesis)
class EffectEvidenceSynthesisAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.EffectEvidenceSynthesis_SampleSize)
class EffectEvidenceSynthesis_SampleSizeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EffectEvidenceSynthesis_ResultsByExposure)
class EffectEvidenceSynthesis_ResultsByExposureAdmin(admin.ModelAdmin):
    list_filter = (
        "exposureState",
    )


@admin.register(models.EffectEvidenceSynthesis_EffectEstimate)
class EffectEvidenceSynthesis_EffectEstimateAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EffectEvidenceSynthesis_PrecisionEstimate)
class EffectEvidenceSynthesis_PrecisionEstimateAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EffectEvidenceSynthesis_Certainty)
class EffectEvidenceSynthesis_CertaintyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EffectEvidenceSynthesis_CertaintySubcomponent)
class EffectEvidenceSynthesis_CertaintySubcomponentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Encounter)
class EncounterAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.Encounter_StatusHistory)
class Encounter_StatusHistoryAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.Encounter_ClassHistory)
class Encounter_ClassHistoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Encounter_Participant)
class Encounter_ParticipantAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Encounter_Diagnosis)
class Encounter_DiagnosisAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Encounter_Hospitalization)
class Encounter_HospitalizationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Encounter_Location)
class Encounter_LocationAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.Endpoint)
class EndpointAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.EnrollmentRequest)
class EnrollmentRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EnrollmentResponse)
class EnrollmentResponseAdmin(admin.ModelAdmin):
    list_filter = (
        "outcome",
    )


@admin.register(models.EpisodeOfCare)
class EpisodeOfCareAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.EpisodeOfCare_StatusHistory)
class EpisodeOfCare_StatusHistoryAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.EpisodeOfCare_Diagnosis)
class EpisodeOfCare_DiagnosisAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EventDefinition)
class EventDefinitionAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.Evidence)
class EvidenceAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.EvidenceVariable)
class EvidenceVariableAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
        "type",
    )


@admin.register(models.EvidenceVariable_Characteristic)
class EvidenceVariable_CharacteristicAdmin(admin.ModelAdmin):
    list_filter = (
        "groupMeasure",
    )


@admin.register(models.ExampleScenario)
class ExampleScenarioAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.ExampleScenario_Actor)
class ExampleScenario_ActorAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.ExampleScenario_Instance)
class ExampleScenario_InstanceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExampleScenario_Version)
class ExampleScenario_VersionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExampleScenario_ContainedInstance)
class ExampleScenario_ContainedInstanceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExampleScenario_Process)
class ExampleScenario_ProcessAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExampleScenario_Step)
class ExampleScenario_StepAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExampleScenario_Operation)
class ExampleScenario_OperationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExampleScenario_Alternative)
class ExampleScenario_AlternativeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExplanationOfBenefit)
class ExplanationOfBenefitAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.ExplanationOfBenefit_Related)
class ExplanationOfBenefit_RelatedAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExplanationOfBenefit_Payee)
class ExplanationOfBenefit_PayeeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExplanationOfBenefit_CareTeam)
class ExplanationOfBenefit_CareTeamAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExplanationOfBenefit_SupportingInfo)
class ExplanationOfBenefit_SupportingInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExplanationOfBenefit_Diagnosis)
class ExplanationOfBenefit_DiagnosisAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExplanationOfBenefit_Procedure)
class ExplanationOfBenefit_ProcedureAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExplanationOfBenefit_Insurance)
class ExplanationOfBenefit_InsuranceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExplanationOfBenefit_Accident)
class ExplanationOfBenefit_AccidentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExplanationOfBenefit_Item)
class ExplanationOfBenefit_ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExplanationOfBenefit_Adjudication)
class ExplanationOfBenefit_AdjudicationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExplanationOfBenefit_Detail)
class ExplanationOfBenefit_DetailAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExplanationOfBenefit_SubDetail)
class ExplanationOfBenefit_SubDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExplanationOfBenefit_AddItem)
class ExplanationOfBenefit_AddItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExplanationOfBenefit_Detail1)
class ExplanationOfBenefit_Detail1Admin(admin.ModelAdmin):
    pass


@admin.register(models.ExplanationOfBenefit_SubDetail1)
class ExplanationOfBenefit_SubDetail1Admin(admin.ModelAdmin):
    pass


@admin.register(models.ExplanationOfBenefit_Total)
class ExplanationOfBenefit_TotalAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExplanationOfBenefit_Payment)
class ExplanationOfBenefit_PaymentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExplanationOfBenefit_ProcessNote)
class ExplanationOfBenefit_ProcessNoteAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.ExplanationOfBenefit_BenefitBalance)
class ExplanationOfBenefit_BenefitBalanceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ExplanationOfBenefit_Financial)
class ExplanationOfBenefit_FinancialAdmin(admin.ModelAdmin):
    pass


@admin.register(models.FamilyMemberHistory)
class FamilyMemberHistoryAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.FamilyMemberHistory_Condition)
class FamilyMemberHistory_ConditionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Flag)
class FlagAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.Goal)
class GoalAdmin(admin.ModelAdmin):
    list_filter = (
        "lifecycleStatus",
    )


@admin.register(models.Goal_Target)
class Goal_TargetAdmin(admin.ModelAdmin):
    pass


@admin.register(models.GraphDefinition)
class GraphDefinitionAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.GraphDefinition_Link)
class GraphDefinition_LinkAdmin(admin.ModelAdmin):
    pass


@admin.register(models.GraphDefinition_Target)
class GraphDefinition_TargetAdmin(admin.ModelAdmin):
    pass


@admin.register(models.GraphDefinition_Compartment)
class GraphDefinition_CompartmentAdmin(admin.ModelAdmin):
    list_filter = (
        "use",
        "rule",
    )


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.Group_Characteristic)
class Group_CharacteristicAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Group_Member)
class Group_MemberAdmin(admin.ModelAdmin):
    pass


@admin.register(models.GuidanceResponse)
class GuidanceResponseAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.HealthcareService)
class HealthcareServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.HealthcareService_Eligibility)
class HealthcareService_EligibilityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.HealthcareService_AvailableTime)
class HealthcareService_AvailableTimeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.HealthcareService_NotAvailable)
class HealthcareService_NotAvailableAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ImagingStudy)
class ImagingStudyAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.ImagingStudy_Series)
class ImagingStudy_SeriesAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ImagingStudy_Performer)
class ImagingStudy_PerformerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ImagingStudy_Instance)
class ImagingStudy_InstanceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Immunization)
class ImmunizationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Immunization_Performer)
class Immunization_PerformerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Immunization_Education)
class Immunization_EducationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Immunization_Reaction)
class Immunization_ReactionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Immunization_ProtocolApplied)
class Immunization_ProtocolAppliedAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ImmunizationEvaluation)
class ImmunizationEvaluationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ImmunizationRecommendation)
class ImmunizationRecommendationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ImmunizationRecommendation_Recommendation)
class ImmunizationRecommendation_RecommendationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ImmunizationRecommendation_DateCriterion)
class ImmunizationRecommendation_DateCriterionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ImplementationGuide)
class ImplementationGuideAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
        "license",
    )


@admin.register(models.ImplementationGuide_DependsOn)
class ImplementationGuide_DependsOnAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ImplementationGuide_Global)
class ImplementationGuide_GlobalAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ImplementationGuide_Definition)
class ImplementationGuide_DefinitionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ImplementationGuide_Grouping)
class ImplementationGuide_GroupingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ImplementationGuide_Resource)
class ImplementationGuide_ResourceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ImplementationGuide_Page)
class ImplementationGuide_PageAdmin(admin.ModelAdmin):
    list_filter = (
        "generation",
    )


@admin.register(models.ImplementationGuide_Parameter)
class ImplementationGuide_ParameterAdmin(admin.ModelAdmin):
    list_filter = (
        "code",
    )


@admin.register(models.ImplementationGuide_Template)
class ImplementationGuide_TemplateAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ImplementationGuide_Manifest)
class ImplementationGuide_ManifestAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ImplementationGuide_Resource1)
class ImplementationGuide_Resource1Admin(admin.ModelAdmin):
    pass


@admin.register(models.ImplementationGuide_Page1)
class ImplementationGuide_Page1Admin(admin.ModelAdmin):
    pass


@admin.register(models.InsurancePlan)
class InsurancePlanAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.InsurancePlan_Contact)
class InsurancePlan_ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(models.InsurancePlan_Coverage)
class InsurancePlan_CoverageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.InsurancePlan_Benefit)
class InsurancePlan_BenefitAdmin(admin.ModelAdmin):
    pass


@admin.register(models.InsurancePlan_Limit)
class InsurancePlan_LimitAdmin(admin.ModelAdmin):
    pass


@admin.register(models.InsurancePlan_Plan)
class InsurancePlan_PlanAdmin(admin.ModelAdmin):
    pass


@admin.register(models.InsurancePlan_GeneralCost)
class InsurancePlan_GeneralCostAdmin(admin.ModelAdmin):
    pass


@admin.register(models.InsurancePlan_SpecificCost)
class InsurancePlan_SpecificCostAdmin(admin.ModelAdmin):
    pass


@admin.register(models.InsurancePlan_Benefit1)
class InsurancePlan_Benefit1Admin(admin.ModelAdmin):
    pass


@admin.register(models.InsurancePlan_Cost)
class InsurancePlan_CostAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.Invoice_Participant)
class Invoice_ParticipantAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Invoice_LineItem)
class Invoice_LineItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Invoice_PriceComponent)
class Invoice_PriceComponentAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.Library)
class LibraryAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.Linkage)
class LinkageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Linkage_Item)
class Linkage_ItemAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
        "mode",
    )


@admin.register(models.List_Entry)
class List_EntryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
        "mode",
    )


@admin.register(models.Location_Position)
class Location_PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Location_HoursOfOperation)
class Location_HoursOfOperationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Measure)
class MeasureAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.Measure_Group)
class Measure_GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Measure_Population)
class Measure_PopulationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Measure_Stratifier)
class Measure_StratifierAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Measure_Component)
class Measure_ComponentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Measure_SupplementalData)
class Measure_SupplementalDataAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MeasureReport)
class MeasureReportAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
        "type",
    )


@admin.register(models.MeasureReport_Group)
class MeasureReport_GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MeasureReport_Population)
class MeasureReport_PopulationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MeasureReport_Stratifier)
class MeasureReport_StratifierAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MeasureReport_Stratum)
class MeasureReport_StratumAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MeasureReport_Component)
class MeasureReport_ComponentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MeasureReport_Population1)
class MeasureReport_Population1Admin(admin.ModelAdmin):
    pass


@admin.register(models.Media)
class MediaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Medication)
class MedicationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Medication_Ingredient)
class Medication_IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Medication_Batch)
class Medication_BatchAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationAdministration)
class MedicationAdministrationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationAdministration_Performer)
class MedicationAdministration_PerformerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationAdministration_Dosage)
class MedicationAdministration_DosageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationDispense)
class MedicationDispenseAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationDispense_Performer)
class MedicationDispense_PerformerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationDispense_Substitution)
class MedicationDispense_SubstitutionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationKnowledge)
class MedicationKnowledgeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationKnowledge_RelatedMedicationKnowledge)
class MedicationKnowledge_RelatedMedicationKnowledgeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationKnowledge_Monograph)
class MedicationKnowledge_MonographAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationKnowledge_Ingredient)
class MedicationKnowledge_IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationKnowledge_Cost)
class MedicationKnowledge_CostAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationKnowledge_MonitoringProgram)
class MedicationKnowledge_MonitoringProgramAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationKnowledge_AdministrationGuidelines)
class MedicationKnowledge_AdministrationGuidelinesAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationKnowledge_Dosage)
class MedicationKnowledge_DosageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationKnowledge_PatientCharacteristics)
class MedicationKnowledge_PatientCharacteristicsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationKnowledge_MedicineClassification)
class MedicationKnowledge_MedicineClassificationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationKnowledge_Packaging)
class MedicationKnowledge_PackagingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationKnowledge_DrugCharacteristic)
class MedicationKnowledge_DrugCharacteristicAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationKnowledge_Regulatory)
class MedicationKnowledge_RegulatoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationKnowledge_Substitution)
class MedicationKnowledge_SubstitutionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationKnowledge_Schedule)
class MedicationKnowledge_ScheduleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationKnowledge_MaxDispense)
class MedicationKnowledge_MaxDispenseAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationKnowledge_Kinetics)
class MedicationKnowledge_KineticsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationRequest)
class MedicationRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationRequest_DispenseRequest)
class MedicationRequest_DispenseRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationRequest_InitialFill)
class MedicationRequest_InitialFillAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationRequest_Substitution)
class MedicationRequest_SubstitutionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicationStatement)
class MedicationStatementAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProduct)
class MedicinalProductAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProduct_Name)
class MedicinalProduct_NameAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProduct_NamePart)
class MedicinalProduct_NamePartAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProduct_CountryLanguage)
class MedicinalProduct_CountryLanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProduct_ManufacturingBusinessOperation)
class MedicinalProduct_ManufacturingBusinessOperationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProduct_SpecialDesignation)
class MedicinalProduct_SpecialDesignationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductAuthorization)
class MedicinalProductAuthorizationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductAuthorization_JurisdictionalAuthorization)
class MedicinalProductAuthorization_JurisdictionalAuthorizationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductAuthorization_Procedure)
class MedicinalProductAuthorization_ProcedureAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductContraindication)
class MedicinalProductContraindicationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductContraindication_OtherTherapy)
class MedicinalProductContraindication_OtherTherapyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductIndication)
class MedicinalProductIndicationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductIndication_OtherTherapy)
class MedicinalProductIndication_OtherTherapyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductIngredient)
class MedicinalProductIngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductIngredient_SpecifiedSubstance)
class MedicinalProductIngredient_SpecifiedSubstanceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductIngredient_Strength)
class MedicinalProductIngredient_StrengthAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductIngredient_ReferenceStrength)
class MedicinalProductIngredient_ReferenceStrengthAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductIngredient_Substance)
class MedicinalProductIngredient_SubstanceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductInteraction)
class MedicinalProductInteractionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductInteraction_Interactant)
class MedicinalProductInteraction_InteractantAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductManufactured)
class MedicinalProductManufacturedAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductPackaged)
class MedicinalProductPackagedAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductPackaged_BatchIdentifier)
class MedicinalProductPackaged_BatchIdentifierAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductPackaged_PackageItem)
class MedicinalProductPackaged_PackageItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductPharmaceutical)
class MedicinalProductPharmaceuticalAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductPharmaceutical_Characteristics)
class MedicinalProductPharmaceutical_CharacteristicsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductPharmaceutical_RouteOfAdministration)
class MedicinalProductPharmaceutical_RouteOfAdministrationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductPharmaceutical_TargetSpecies)
class MedicinalProductPharmaceutical_TargetSpeciesAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductPharmaceutical_WithdrawalPeriod)
class MedicinalProductPharmaceutical_WithdrawalPeriodAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicinalProductUndesirableEffect)
class MedicinalProductUndesirableEffectAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MessageDefinition)
class MessageDefinitionAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
        "category",
        "responseRequired",
    )


@admin.register(models.MessageDefinition_Focus)
class MessageDefinition_FocusAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MessageDefinition_AllowedResponse)
class MessageDefinition_AllowedResponseAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MessageHeader)
class MessageHeaderAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MessageHeader_Destination)
class MessageHeader_DestinationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MessageHeader_Source)
class MessageHeader_SourceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MessageHeader_Response)
class MessageHeader_ResponseAdmin(admin.ModelAdmin):
    list_filter = (
        "code",
    )


@admin.register(models.MolecularSequence)
class MolecularSequenceAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.MolecularSequence_ReferenceSeq)
class MolecularSequence_ReferenceSeqAdmin(admin.ModelAdmin):
    list_filter = (
        "orientation",
        "strand",
    )


@admin.register(models.MolecularSequence_Variant)
class MolecularSequence_VariantAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MolecularSequence_Quality)
class MolecularSequence_QualityAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.MolecularSequence_Roc)
class MolecularSequence_RocAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MolecularSequence_Repository)
class MolecularSequence_RepositoryAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.MolecularSequence_StructureVariant)
class MolecularSequence_StructureVariantAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MolecularSequence_Outer)
class MolecularSequence_OuterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MolecularSequence_Inner)
class MolecularSequence_InnerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.NamingSystem)
class NamingSystemAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
        "kind",
    )


@admin.register(models.NamingSystem_UniqueId)
class NamingSystem_UniqueIdAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.NutritionOrder)
class NutritionOrderAdmin(admin.ModelAdmin):
    pass


@admin.register(models.NutritionOrder_OralDiet)
class NutritionOrder_OralDietAdmin(admin.ModelAdmin):
    pass


@admin.register(models.NutritionOrder_Nutrient)
class NutritionOrder_NutrientAdmin(admin.ModelAdmin):
    pass


@admin.register(models.NutritionOrder_Texture)
class NutritionOrder_TextureAdmin(admin.ModelAdmin):
    pass


@admin.register(models.NutritionOrder_Supplement)
class NutritionOrder_SupplementAdmin(admin.ModelAdmin):
    pass


@admin.register(models.NutritionOrder_EnteralFormula)
class NutritionOrder_EnteralFormulaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.NutritionOrder_Administration)
class NutritionOrder_AdministrationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Observation)
class ObservationAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.Observation_ReferenceRange)
class Observation_ReferenceRangeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Observation_Component)
class Observation_ComponentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ObservationDefinition)
class ObservationDefinitionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ObservationDefinition_QuantitativeDetails)
class ObservationDefinition_QuantitativeDetailsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ObservationDefinition_QualifiedInterval)
class ObservationDefinition_QualifiedIntervalAdmin(admin.ModelAdmin):
    list_filter = (
        "category",
        "gender",
    )


@admin.register(models.OperationDefinition)
class OperationDefinitionAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
        "kind",
    )


@admin.register(models.OperationDefinition_Parameter)
class OperationDefinition_ParameterAdmin(admin.ModelAdmin):
    list_filter = (
        "use",
        "searchType",
    )


@admin.register(models.OperationDefinition_Binding)
class OperationDefinition_BindingAdmin(admin.ModelAdmin):
    list_filter = (
        "strength",
    )


@admin.register(models.OperationDefinition_ReferencedFrom)
class OperationDefinition_ReferencedFromAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OperationDefinition_Overload)
class OperationDefinition_OverloadAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OperationOutcome)
class OperationOutcomeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OperationOutcome_Issue)
class OperationOutcome_IssueAdmin(admin.ModelAdmin):
    list_filter = (
        "severity",
        "code",
    )


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Organization_Contact)
class Organization_ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OrganizationAffiliation)
class OrganizationAffiliationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Parameters)
class ParametersAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Parameters_Parameter)
class Parameters_ParameterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    list_filter = (
        "gender",
    )


@admin.register(models.Patient_Contact)
class Patient_ContactAdmin(admin.ModelAdmin):
    list_filter = (
        "gender",
    )


@admin.register(models.Patient_Communication)
class Patient_CommunicationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Patient_Link)
class Patient_LinkAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.PaymentNotice)
class PaymentNoticeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PaymentReconciliation)
class PaymentReconciliationAdmin(admin.ModelAdmin):
    list_filter = (
        "outcome",
    )


@admin.register(models.PaymentReconciliation_Detail)
class PaymentReconciliation_DetailAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PaymentReconciliation_ProcessNote)
class PaymentReconciliation_ProcessNoteAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_filter = (
        "gender",
    )


@admin.register(models.Person_Link)
class Person_LinkAdmin(admin.ModelAdmin):
    list_filter = (
        "assurance",
    )


@admin.register(models.PlanDefinition)
class PlanDefinitionAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.PlanDefinition_Goal)
class PlanDefinition_GoalAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PlanDefinition_Target)
class PlanDefinition_TargetAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PlanDefinition_Action)
class PlanDefinition_ActionAdmin(admin.ModelAdmin):
    list_filter = (
        "groupingBehavior",
        "selectionBehavior",
        "requiredBehavior",
        "precheckBehavior",
        "cardinalityBehavior",
    )


@admin.register(models.PlanDefinition_Condition)
class PlanDefinition_ConditionAdmin(admin.ModelAdmin):
    list_filter = (
        "kind",
    )


@admin.register(models.PlanDefinition_RelatedAction)
class PlanDefinition_RelatedActionAdmin(admin.ModelAdmin):
    list_filter = (
        "relationship",
    )


@admin.register(models.PlanDefinition_Participant)
class PlanDefinition_ParticipantAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.PlanDefinition_DynamicValue)
class PlanDefinition_DynamicValueAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Practitioner)
class PractitionerAdmin(admin.ModelAdmin):
    list_filter = (
        "gender",
    )


@admin.register(models.Practitioner_Qualification)
class Practitioner_QualificationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PractitionerRole)
class PractitionerRoleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PractitionerRole_AvailableTime)
class PractitionerRole_AvailableTimeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PractitionerRole_NotAvailable)
class PractitionerRole_NotAvailableAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Procedure_Performer)
class Procedure_PerformerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Procedure_FocalDevice)
class Procedure_FocalDeviceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Provenance)
class ProvenanceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Provenance_Agent)
class Provenance_AgentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Provenance_Entity)
class Provenance_EntityAdmin(admin.ModelAdmin):
    list_filter = (
        "role",
    )


@admin.register(models.Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.Questionnaire_Item)
class Questionnaire_ItemAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
        "enableBehavior",
    )


@admin.register(models.Questionnaire_EnableWhen)
class Questionnaire_EnableWhenAdmin(admin.ModelAdmin):
    list_filter = (
        "operator",
    )


@admin.register(models.Questionnaire_AnswerOption)
class Questionnaire_AnswerOptionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Questionnaire_Initial)
class Questionnaire_InitialAdmin(admin.ModelAdmin):
    pass


@admin.register(models.QuestionnaireResponse)
class QuestionnaireResponseAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.QuestionnaireResponse_Item)
class QuestionnaireResponse_ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.QuestionnaireResponse_Answer)
class QuestionnaireResponse_AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RelatedPerson)
class RelatedPersonAdmin(admin.ModelAdmin):
    list_filter = (
        "gender",
    )


@admin.register(models.RelatedPerson_Communication)
class RelatedPerson_CommunicationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RequestGroup)
class RequestGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RequestGroup_Action)
class RequestGroup_ActionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RequestGroup_Condition)
class RequestGroup_ConditionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RequestGroup_RelatedAction)
class RequestGroup_RelatedActionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ResearchDefinition)
class ResearchDefinitionAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.ResearchElementDefinition)
class ResearchElementDefinitionAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
        "type",
        "variableType",
    )


@admin.register(models.ResearchElementDefinition_Characteristic)
class ResearchElementDefinition_CharacteristicAdmin(admin.ModelAdmin):
    list_filter = (
        "studyEffectiveGroupMeasure",
        "participantEffectiveGroupMeasure",
    )


@admin.register(models.ResearchStudy)
class ResearchStudyAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.ResearchStudy_Arm)
class ResearchStudy_ArmAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ResearchStudy_Objective)
class ResearchStudy_ObjectiveAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ResearchSubject)
class ResearchSubjectAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.RiskAssessment)
class RiskAssessmentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RiskAssessment_Prediction)
class RiskAssessment_PredictionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RiskEvidenceSynthesis)
class RiskEvidenceSynthesisAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.RiskEvidenceSynthesis_SampleSize)
class RiskEvidenceSynthesis_SampleSizeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RiskEvidenceSynthesis_RiskEstimate)
class RiskEvidenceSynthesis_RiskEstimateAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RiskEvidenceSynthesis_PrecisionEstimate)
class RiskEvidenceSynthesis_PrecisionEstimateAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RiskEvidenceSynthesis_Certainty)
class RiskEvidenceSynthesis_CertaintyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RiskEvidenceSynthesis_CertaintySubcomponent)
class RiskEvidenceSynthesis_CertaintySubcomponentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SearchParameter)
class SearchParameterAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
        "type",
        "xpathUsage",
    )


@admin.register(models.SearchParameter_Component)
class SearchParameter_ComponentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Slot)
class SlotAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.Specimen)
class SpecimenAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.Specimen_Collection)
class Specimen_CollectionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Specimen_Processing)
class Specimen_ProcessingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Specimen_Container)
class Specimen_ContainerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SpecimenDefinition)
class SpecimenDefinitionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SpecimenDefinition_TypeTested)
class SpecimenDefinition_TypeTestedAdmin(admin.ModelAdmin):
    list_filter = (
        "preference",
    )


@admin.register(models.SpecimenDefinition_Container)
class SpecimenDefinition_ContainerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SpecimenDefinition_Additive)
class SpecimenDefinition_AdditiveAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SpecimenDefinition_Handling)
class SpecimenDefinition_HandlingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.StructureDefinition)
class StructureDefinitionAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
        "fhirVersion",
        "kind",
        "derivation",
    )


@admin.register(models.StructureDefinition_Mapping)
class StructureDefinition_MappingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.StructureDefinition_Context)
class StructureDefinition_ContextAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.StructureDefinition_Snapshot)
class StructureDefinition_SnapshotAdmin(admin.ModelAdmin):
    pass


@admin.register(models.StructureDefinition_Differential)
class StructureDefinition_DifferentialAdmin(admin.ModelAdmin):
    pass


@admin.register(models.StructureMap)
class StructureMapAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.StructureMap_Structure)
class StructureMap_StructureAdmin(admin.ModelAdmin):
    list_filter = (
        "mode",
    )


@admin.register(models.StructureMap_Group)
class StructureMap_GroupAdmin(admin.ModelAdmin):
    list_filter = (
        "typeMode",
    )


@admin.register(models.StructureMap_Input)
class StructureMap_InputAdmin(admin.ModelAdmin):
    list_filter = (
        "mode",
    )


@admin.register(models.StructureMap_Rule)
class StructureMap_RuleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.StructureMap_Source)
class StructureMap_SourceAdmin(admin.ModelAdmin):
    list_filter = (
        "listMode",
    )


@admin.register(models.StructureMap_Target)
class StructureMap_TargetAdmin(admin.ModelAdmin):
    list_filter = (
        "contextType",
        "transform",
    )


@admin.register(models.StructureMap_Parameter)
class StructureMap_ParameterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.StructureMap_Dependent)
class StructureMap_DependentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.Subscription_Channel)
class Subscription_ChannelAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.Substance)
class SubstanceAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.Substance_Instance)
class Substance_InstanceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Substance_Ingredient)
class Substance_IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceNucleicAcid)
class SubstanceNucleicAcidAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceNucleicAcid_Subunit)
class SubstanceNucleicAcid_SubunitAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceNucleicAcid_Linkage)
class SubstanceNucleicAcid_LinkageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceNucleicAcid_Sugar)
class SubstanceNucleicAcid_SugarAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstancePolymer)
class SubstancePolymerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstancePolymer_MonomerSet)
class SubstancePolymer_MonomerSetAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstancePolymer_StartingMaterial)
class SubstancePolymer_StartingMaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstancePolymer_Repeat)
class SubstancePolymer_RepeatAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstancePolymer_RepeatUnit)
class SubstancePolymer_RepeatUnitAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstancePolymer_DegreeOfPolymerisation)
class SubstancePolymer_DegreeOfPolymerisationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstancePolymer_StructuralRepresentation)
class SubstancePolymer_StructuralRepresentationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceProtein)
class SubstanceProteinAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceProtein_Subunit)
class SubstanceProtein_SubunitAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceReferenceInformation)
class SubstanceReferenceInformationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceReferenceInformation_Gene)
class SubstanceReferenceInformation_GeneAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceReferenceInformation_GeneElement)
class SubstanceReferenceInformation_GeneElementAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceReferenceInformation_Classification)
class SubstanceReferenceInformation_ClassificationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceReferenceInformation_Target)
class SubstanceReferenceInformation_TargetAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceSourceMaterial)
class SubstanceSourceMaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceSourceMaterial_FractionDescription)
class SubstanceSourceMaterial_FractionDescriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceSourceMaterial_Organism)
class SubstanceSourceMaterial_OrganismAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceSourceMaterial_Author)
class SubstanceSourceMaterial_AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceSourceMaterial_Hybrid)
class SubstanceSourceMaterial_HybridAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceSourceMaterial_OrganismGeneral)
class SubstanceSourceMaterial_OrganismGeneralAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceSourceMaterial_PartDescription)
class SubstanceSourceMaterial_PartDescriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceSpecification)
class SubstanceSpecificationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceSpecification_Moiety)
class SubstanceSpecification_MoietyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceSpecification_Property)
class SubstanceSpecification_PropertyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceSpecification_Structure)
class SubstanceSpecification_StructureAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceSpecification_Isotope)
class SubstanceSpecification_IsotopeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceSpecification_MolecularWeight)
class SubstanceSpecification_MolecularWeightAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceSpecification_Representation)
class SubstanceSpecification_RepresentationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceSpecification_Code)
class SubstanceSpecification_CodeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceSpecification_Name)
class SubstanceSpecification_NameAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceSpecification_Official)
class SubstanceSpecification_OfficialAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubstanceSpecification_Relationship)
class SubstanceSpecification_RelationshipAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SupplyDelivery)
class SupplyDeliveryAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.SupplyDelivery_SuppliedItem)
class SupplyDelivery_SuppliedItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SupplyRequest)
class SupplyRequestAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.SupplyRequest_Parameter)
class SupplyRequest_ParameterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
        "intent",
    )


@admin.register(models.Task_Restriction)
class Task_RestrictionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Task_Input)
class Task_InputAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Task_Output)
class Task_OutputAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TerminologyCapabilities)
class TerminologyCapabilitiesAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
        "codeSearch",
    )


@admin.register(models.TerminologyCapabilities_Software)
class TerminologyCapabilities_SoftwareAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TerminologyCapabilities_Implementation)
class TerminologyCapabilities_ImplementationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TerminologyCapabilities_CodeSystem)
class TerminologyCapabilities_CodeSystemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TerminologyCapabilities_Version)
class TerminologyCapabilities_VersionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TerminologyCapabilities_Filter)
class TerminologyCapabilities_FilterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TerminologyCapabilities_Expansion)
class TerminologyCapabilities_ExpansionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TerminologyCapabilities_Parameter)
class TerminologyCapabilities_ParameterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TerminologyCapabilities_ValidateCode)
class TerminologyCapabilities_ValidateCodeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TerminologyCapabilities_Translation)
class TerminologyCapabilities_TranslationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TerminologyCapabilities_Closure)
class TerminologyCapabilities_ClosureAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TestReport)
class TestReportAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
        "result",
    )


@admin.register(models.TestReport_Participant)
class TestReport_ParticipantAdmin(admin.ModelAdmin):
    list_filter = (
        "type",
    )


@admin.register(models.TestReport_Setup)
class TestReport_SetupAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TestReport_Action)
class TestReport_ActionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TestReport_Operation)
class TestReport_OperationAdmin(admin.ModelAdmin):
    list_filter = (
        "result",
    )


@admin.register(models.TestReport_Assert)
class TestReport_AssertAdmin(admin.ModelAdmin):
    list_filter = (
        "result",
    )


@admin.register(models.TestReport_Test)
class TestReport_TestAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TestReport_Action1)
class TestReport_Action1Admin(admin.ModelAdmin):
    pass


@admin.register(models.TestReport_Teardown)
class TestReport_TeardownAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TestReport_Action2)
class TestReport_Action2Admin(admin.ModelAdmin):
    pass


@admin.register(models.TestScript)
class TestScriptAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.TestScript_Origin)
class TestScript_OriginAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TestScript_Destination)
class TestScript_DestinationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TestScript_Metadata)
class TestScript_MetadataAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TestScript_Link)
class TestScript_LinkAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TestScript_Capability)
class TestScript_CapabilityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TestScript_Fixture)
class TestScript_FixtureAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TestScript_Variable)
class TestScript_VariableAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TestScript_Setup)
class TestScript_SetupAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TestScript_Action)
class TestScript_ActionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TestScript_Operation)
class TestScript_OperationAdmin(admin.ModelAdmin):
    list_filter = (
        "method",
    )


@admin.register(models.TestScript_RequestHeader)
class TestScript_RequestHeaderAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TestScript_Assert)
class TestScript_AssertAdmin(admin.ModelAdmin):
    list_filter = (
        "direction",
        "operator",
        "requestMethod",
        "response",
    )


@admin.register(models.TestScript_Test)
class TestScript_TestAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TestScript_Action1)
class TestScript_Action1Admin(admin.ModelAdmin):
    pass


@admin.register(models.TestScript_Teardown)
class TestScript_TeardownAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TestScript_Action2)
class TestScript_Action2Admin(admin.ModelAdmin):
    pass


@admin.register(models.ValueSet)
class ValueSetAdmin(admin.ModelAdmin):
    list_filter = (
        "status",
    )


@admin.register(models.ValueSet_Compose)
class ValueSet_ComposeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ValueSet_Include)
class ValueSet_IncludeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ValueSet_Concept)
class ValueSet_ConceptAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ValueSet_Designation)
class ValueSet_DesignationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ValueSet_Filter)
class ValueSet_FilterAdmin(admin.ModelAdmin):
    list_filter = (
        "op",
    )


@admin.register(models.ValueSet_Expansion)
class ValueSet_ExpansionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ValueSet_Parameter)
class ValueSet_ParameterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ValueSet_Contains)
class ValueSet_ContainsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.VerificationResult)
class VerificationResultAdmin(admin.ModelAdmin):
    pass


@admin.register(models.VerificationResult_PrimarySource)
class VerificationResult_PrimarySourceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.VerificationResult_Attestation)
class VerificationResult_AttestationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.VerificationResult_Validator)
class VerificationResult_ValidatorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.VisionPrescription)
class VisionPrescriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.VisionPrescription_LensSpecification)
class VisionPrescription_LensSpecificationAdmin(admin.ModelAdmin):
    list_filter = (
        "eye",
    )


@admin.register(models.VisionPrescription_Prism)
class VisionPrescription_PrismAdmin(admin.ModelAdmin):
    list_filter = (
        "base",
    )
