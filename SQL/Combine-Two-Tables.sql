Select firstName, lastName, city, state
From Person
Left JOIN Address
On Person.personID = Address.personID
