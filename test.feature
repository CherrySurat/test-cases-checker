Feature: Sign up to pomelo fashion app

    @Signup
    Scenario: Sign up by email - sccuess case
        Given input credential 
        When Click email button
        And Fill in the email from <email> 
        And Click continued 
        Examples:
        | test_id | test_case                         | email                | first_name                            | last_name                            | phone_no   | password   |
        | TC01    | success - login successfully      | nice.t@email.com     | testfirstnameshouldmorethanthirdtee  | testlastnameshouldmorethanthirdtees   | 8888888888 | Pomelo123* |
        | TC02    | failed  - Test cases1 login       | nice.t@email.com     | testfirstnameshouldmorethanthirdtee  | testlastnameshouldmorethanthirdtees   | 8888888888 | Pomelo123* |
        | TC03    | failed  - Test cases2 login       | nice.t@email.com     | testfirstnameshouldmorethanthirdtee  | testlastnameshouldmorethanthirdtees   | 8888888888 | Pomelo123* |
        | TC04    | failed  - Test cases3 login       | nice.t@email.com     | testfirstnameshouldmorethanthirdtee  | testlastnameshouldmorethanthirdtees   | 8888888888 | Pomelo123* |
        | TC05    | failed  - Test cases4 login       | nice.t@email.com     | testfirstnameshouldmorethanthirdtee  | testlastnameshouldmorethanthirdtees   | 8888888888 | Pomelo123* |
