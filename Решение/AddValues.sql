use PlaceList
go

BULK
INSERT GeoPositions
FROM 'E:\Education\yourself\for_Softech\Test\�������\GeoPositionList.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO

BULK
INSERT CategoryList
FROM 'E:\Education\yourself\for_Softech\Test\�������\CategoryList.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO

BULK
INSERT Categories
FROM 'E:\Education\yourself\for_Softech\Test\�������\Category.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO

BULK
INSERT [Address]
FROM 'E:\Education\yourself\for_Softech\Test\�������\Adress.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO

BULK
INSERT AdminNames
FROM 'E:\Education\yourself\for_Softech\Test\�������\AdminNameList.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO

BULK
INSERT ContactList
FROM 'E:\Education\yourself\for_Softech\Test\�������\ContactList.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO

BULK
INSERT Contacts
FROM 'E:\Education\yourself\for_Softech\Test\�������\Contact.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO

BULK
INSERT CountryCodes
FROM 'E:\Education\yourself\for_Softech\Test\�������\CountryCodes.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO

BULK
INSERT Locations
FROM 'E:\Education\yourself\for_Softech\Test\�������\LocationList.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO

BULK
INSERT Names
FROM 'E:\Education\yourself\for_Softech\Test\�������\NameList.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO

BULK
INSERT Places
FROM 'E:\Education\yourself\for_Softech\Test\�������\PlaceList.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO

BULK
INSERT Streets
FROM 'E:\Education\yourself\for_Softech\Test\�������\StreetNames.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO