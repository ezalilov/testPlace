use PlaceList
go

-- Найти все адреса у Places, имеющих 'CategoryId'=9567 в 'categorySystem'='poi'.
-- Сформируйте адресные строки для найденных Places.

select BaseName, StreetType, HouseNumber,NameLevel1,NameLevel2,NameLevel3,NameLevel4
from Address a join Streets s on a.StreetId=s.StreetId join AdminNames aN on a.AdminNameId=aN.AdminNameId
join Locations l on l.AddressId = a.AddressId join Places p on p.LocationId=l.LocationId join CategoryList cL 
on p.CategoryListId=cL.CategoryListId join Categories c on c.CategoryListId=cL.CategoryListId
 where Category='9567' and categorySystem='poi'
 go

 --	Найти все имена Places, имеющих 'CountryCode'='RUS' и непустой WEBADDRESS

 select BaseText from Names n join Places p on n.NameId=p.NameId join Locations l on p.LocationId=l.LocationId join Address a 
 on l.AddressId=a.AddressId join CountryCodes cc on cc.CountryCodeId=a.CountryCodeId join ContactList cl 
 on p.ContactListId=cl.ContactListId join Contacts c on c.ContactListId=cl.ContactListId
 where CountryCode='RUS' and ContactType='WEBADDRESS' and ContactString is not null
 go
