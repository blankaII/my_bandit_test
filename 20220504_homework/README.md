

     ┌────┐                      ┌────┐          ┌────┐                ┌──┐             ┌──────┐                                      ┌───────────┐
     │User│                      │WebA│          │WebB│                │DB│             │Bandit│                                      │Web_Breeder│
     └─┬──┘                      └─┬──┘          └─┬──┘                └┬─┘             └──┬───┘                                      └─────┬─────┘
       │ 30% choose A, 10% choose B│               │                    │                  │                                                │      
       │ ──────────────────────────>               │                    │                  │                                                │      
       │                           │               │                    │                  │                                                │      
       │         10% choose A, 30% choose B        │                    │                  │                                                │      
       │ ──────────────────────────────────────────>                    │                  │                                                │      
       │                           │               │                    │                  │                                                │      
       │                           │         store click history        │                  │                                                │      
       │                           │ ───────────────────────────────────>                  │                                                │      
       │                           │               │                    │                  │                                                │      
       │                           │               │ store click history│                  │                                                │      
       │                           │               │ ───────────────────>                  │                                                │      
       │                           │               │                    │                  │                                                │      
       │                           │               │                    │ AB test algorithm│                                                │      
       │                           │               │                    │ ─────────────────>                                                │      
       │                           │               │                    │                  │                                                │      
       │                           │               │                    │                  │ feedback WebA or WebB base on result of AB test│      
       │                           │               │                    │                  │ ───────────────────────────────────────────────>      
       │                           │               │                    │                  │                                                │      
       │                           │               │           feedback greedy option      │                                                │      
       │ <───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────      
     ┌─┴──┐                      ┌─┴──┐          ┌─┴──┐                ┌┴─┐             ┌──┴───┐                                      ┌─────┴─────┐
     │User│                      │WebA│          │WebB│                │DB│             │Bandit│                                      │Web_Breeder│
     └────┘                      └────┘          └────┘                └──┘             └──────┘                                      └───────────┘

################################################################################
- http://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000

<p><code>
@startuml
User -> WebA : 30% choose A, 10% choose B
User -> WebB : 10% choose A, 30% choose B
WebA -> DB : store click history
WebB -> DB : store click history
DB -> Bandit : AB test algorithm
Bandit -> Web_Breeder : feedback WebA or WebB base on result of AB test
Web_Breeder -> User : feedback greedy option
@enduml
</code></p>
