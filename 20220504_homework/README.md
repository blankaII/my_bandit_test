     ┌────┐                      ┌────┐          ┌────┐          ┌─────────┐             ┌──┐             ┌──────┐           ┌───────────┐
     │User│                      │WebA│          │WebB│          │Collector│             │DB│             │Bandit│           │Web_Breeder│
     └─┬──┘                      └─┬──┘          └─┬──┘          └────┬────┘             └┬─┘             └──┬───┘           └─────┬─────┘
       │ 30% choose A, 10% choose B│               │                  │                   │                  │                     │      
       │ ──────────────────────────>               │                  │                   │                  │                     │      
       │                           │               │                  │                   │                  │                     │      
       │         10% choose A, 30% choose B        │                  │                   │                  │                     │      
       │ ──────────────────────────────────────────>                  │                   │                  │                     │      
       │                           │               │                  │                   │                  │                     │      
       │                           │           json from A            │                   │                  │                     │      
       │                           │ ────────────────────────────────>│                   │                  │                     │      
       │                           │               │                  │                   │                  │                     │      
       │                           │               │   json from B    │                   │                  │                     │      
       │                           │               │ ────────────────>│                   │                  │                     │      
       │                           │               │                  │                   │                  │                     │      
       │                           │               │                  │click history to DB│                  │                     │      
       │                           │               │                  │───────────────────>                  │                     │      
       │                           │               │                  │                   │                  │                     │      
       │                           │               │                  │                   │ AB test algorithm│                     │      
       │                           │               │                  │                   │ ─────────────────>                     │      
       │                           │               │                  │                   │                  │                     │      
       │                           │               │                  │                   │                  │ Better WebA or WebB │      
       │                           │               │                  │                   │                  │ ───────────────────>│      
       │                           │               │                  │                   │                  │                     │      
       │                           │               │             read Web                 │                  │                     │      
       │ <─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────│      
     ┌─┴──┐                      ┌─┴──┐          ┌─┴──┐          ┌────┴────┐             ┌┴─┐             ┌──┴───┐           ┌─────┴─────┐
     │User│                      │WebA│          │WebB│          │Collector│             │DB│             │Bandit│           │Web_Breeder│
     └────┘                      └────┘          └────┘          └─────────┘             └──┘             └──────┘           └───────────┘
################################################################################
- http://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000

<p><code>
@startuml
User -> WebA : 30% choose A, 10% choose B
User -> WebB : 10% choose A, 30% choose B
WebA -> Collector : json from A
WebB -> Collector : json from B
Collector -> DB : click history to DB
DB -> Bandit : AB test algorithm
Bandit -> Web_Breeder : Better WebA or WebB
Web_Breeder -> User : read Web
@enduml
</code></p>
