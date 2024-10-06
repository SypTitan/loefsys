```mermaid
classDiagram

    class Contact {
        email : EmailField
        receive_newsletter : bool
        phone_number : str | null
        note : TextField

        address : Address | null
        person: Person | null
        organization: Organization | null
    }

    class Address {
        contact : Contact

        street : CharField
        street2 : CharField
        postal_code : CharField
        city : CharField
        country : CharField
    }

    class Person {
        contact : ContactDetails

        first_name : str
        last_name : str
        initials : str
        nickname : str
        display_name_preference : enum
        display_name : str

        memberdetails : MemberDetails | null
    }

    class Organization {
        contact : ContactDetails
        name : str
        website : str
    }

    class LoefbijterMember {
        person : PersonDetails
        gender : enum
        birthday : date
        show_birthday : bool
        studyregistration : StudyRegistration | null
        membership_set : QuerySet[Membership]
    }

    class StudyRegistration {
        member : MemberDetails

        institution : str
        programme : str
        student_number : str
        rsc_number : str
    }

    class Membership {
        person : Person
        membership_type : enum
        start : date
        end : date | null
    }

    Contact <-- Address : One to One
    Contact <-- Organization : One to One
    Contact <-- Person : One to One
    Person <-- Member : One to One
    Member o-- Membership : One to Many
    Member <-- StudyRegistration : One to One
```
