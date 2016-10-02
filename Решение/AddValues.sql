use PlaceList
go

BULK
INSERT GeoPositions
FROM 'E:\Education\yourself\for_Softech\Test\Place.csv'
WITH
(
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n'
)
GO

BULK
INSERT CategoryList
FROM 'E:\Education\yourself\for_Softech\Test\CategoryList.csv'
WITH
(
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n'
)
GO