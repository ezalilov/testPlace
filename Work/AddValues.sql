use PlaceList
go

BULK
INSERT GeoPositions
FROM 'E:\Education\yourself\for_Softech\Test\Work\GeoPositionList.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO

BULK
INSERT CategoryList
FROM 'E:\Education\yourself\for_Softech\Test\Work\CategoryList.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO

BULK
INSERT Categories
FROM 'E:\Education\yourself\for_Softech\Test\Work\Category.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO

BULK
INSERT [Address]
FROM 'E:\Education\yourself\for_Softech\Test\Work\Adress.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO

BULK
INSERT AdminNames
FROM 'E:\Education\yourself\for_Softech\Test\Work\AdminNameList.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO

BULK
INSERT ContactList
FROM 'E:\Education\yourself\for_Softech\Test\Work\ContactList.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO

BULK
INSERT Contacts
FROM 'E:\Education\yourself\for_Softech\Test\Work\Contact.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO

BULK
INSERT CountryCodes
FROM 'E:\Education\yourself\for_Softech\Test\Work\CountryCodes.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO

BULK
INSERT Locations
FROM 'E:\Education\yourself\for_Softech\Test\Work\LocationList.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO

BULK
INSERT Names
FROM 'E:\Education\yourself\for_Softech\Test\Work\NameList.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO

BULK
INSERT Places
FROM 'E:\Education\yourself\for_Softech\Test\Work\PlaceList.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO

BULK
INSERT Streets
FROM 'E:\Education\yourself\for_Softech\Test\Work\StreetNames.csv'
WITH
(FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO