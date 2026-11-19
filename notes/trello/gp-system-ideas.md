# Not An Open Source GP Clinical System

Snapshot of cards from <https://trello.com/b/g593r5Wm/not-an-open-source-gp-clinical-system>, captured 2026-04-22.

## Ideas

1. INRstar's disclaimer
2. One-click referrals — with context sensitivity to coded items in the current consultation.
3. Telephone integration — 'click to call this patient' — routing either to an IP phone or using a WebRTC service
4. SMS integration — 'click to text'
5. Patient information — 'click to send via SMS/email'
6. Large file sharing

## Making my life easier as a GP

1. Real-time pharmacy stock notifications for shortages — lets you know at point of prescription what is out of stock locally/nationally
2. Safe, clinically assured, peer-reviewed and scrutinised open source clinical calculations, and codelists
3. Regularly-updated, clinically assured, Pathways for investigating and treating a symptom/sign/condition

## Making admin easier

1. Full-record viewing for patients (nothing redacted)

## Killer features

1. Telephone integration — 'click to call this patient' — routing either to an IP phone or using a WebRTC service
2. Open source chat app integration (Rocket/Mattermost)
3. Export of anonymised analytics data to appraisal portfolio — auto-generated reports for prescribing, case-mix, and areas to focus learning
4. Preset Triage Buttons — Dr can review & click — allows admin to call pt back to arrange an appointment when one is clearly necessary from the reception note
5. Medical Markdown for rapid structured data entry
6. Keyboard shortcuts everywhere
7. **Everything** has a URL — you can link any entity in the medical record to any other. For example a change of medication can be linked to the letter that requested the change of medication
8. Scanned Document inline thumbnails — mouseover previews — pop-up rapid view
9. Pregnant patient alert in UI and automatic pregnancy weeks tracker in top bar once EDD is entered

## Culture and Philosophy of the project

1. There's only ONE version — the awesome version. No 'community edition' cut-down release, no Pro upgrade, no disabled features. 100% open source and free from the first commit onwards
2. Remember most recent actions of a user and 'learn' your habits, patterns, and favourites, showing you these first
3. Treat your users as professionals with brains. They can handle features that give them power and they can be trusted to use these features responsibly
4. Wrap anything 'hard' (Spine access, N3 comms, SmartCards, GP Connect, GP2GP...) in a gem, API or Docker container, extract it and release for reuse

## Cutting edge EHR infrastructure

1. openEHR archetypes on IPFS
2. FHIR interface to Rails business logic layer
3. REST API middleware/data streaming layer
4. Component-based responsive Ember.js UI with plugin outlets for customisation and extension
5. Hash-based trustless audit trail
6. NHS Login for patient access
7. NHS Identity for staff login
8. Local & national prescribing guidelines can be distributed via a cascading lookup (local overrides national IF set)

## UI rules

1. NO BLOCKING MODALS
2. NO CLICK-TO-DISMISS INFORMATIONAL DIALOGS
3. CAN BE 100% KEYBOARD DRIVEN
4. RESPONSIVE OOTB

## Resources

### INRstar's disclaimer

> This Product is intended to aid and supplement, not substitute for, the expertise and judgment of physicians, pharmacists or other healthcare professionals. All information is provided on the basis that the healthcare practitioners responsible for patient care will retain full and sole responsibility for deciding any treatment to prescribe or dispense for all patients and, in particular whether the use of information provided by this Product is safe, appropriate, or effective for any particular patient or in any particular circumstances. Logging into INRstar will be taken as your acceptance of this statement.
