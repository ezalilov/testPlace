create database PlaceList
go
use test
go
drop database PlaceList
go
use [PlaceList]
go

create table [dbo].[Places](
	PlaceId int not null primary key,
	[TimeStamp] timestamp not null,
	LocationId int not null,
	ContactId int not null,
	NameId int not null,
	CategoryListId int not null	
)
go

create table [dbo].[Locations](
	LocationId int primary key not null,
	AddressId int not null,
	GeoPositionId int not null
)
go

create table dbo.[Address](
	AddressId int primary key not null,
	StreetId int not null,
	HouseNumber varchar(6),
	CountryCodeId int not null,
	AdminNameId int not null,
	PostalCode int
)
go

create table dbo.GeoPositions(
	GeoPositionId int primary key not null,
	Latitude float(24) not null,
	Longitude float(24) not null,
/*	Altitude int */
)
go

alter table Locations
add constraint fk_AddressId foreign key (AddressId)
	references [Address] (AddressId),

	constraint fk_GeoPositionId foreign key (GeoPositionId)
	references GeoPositions (GeoPositionId)
go

create table [dbo].[Streets](
	StreetId int primary key not null,
	BaseName varchar(50) not null,
	StreetType varchar(20)
)
go

create table [dbo].[CountryCodes](
	CountryCodeId int primary key not null,
	CountryCode varchar(3) not null,
	AdminLevel1 varchar(20),
	AdminLevel2 varchar(20),
	AdminLevel3 varchar(20),
	AdminLevel4 varchar(20),
)
go

create table dbo.AdminNames(
	AdminNameId int primary key not null,
	NameLevel1 varchar(20),
	NameLevel2 varchar(20),
	NameLevel3 varchar(20),
	NameLevel4 varchar(20)
)
go

alter table [Address]
add constraint fk_StreetId foreign key (StreetId)
	references Streets (StreetId),

	constraint fk_CountryCodeId foreign key (CountryCodeId)
	references CountryCodes (CountryCodeId),

	constraint fk_AdminNameId foreign key (AdminNameId)
	references AdminNames (AdminNameId)
go

create table [dbo].[Contacts](
	ContactId int primary key not null,
	ContactType varchar(20) not null,
	ContactString varchar(50) not null
)
go

create table [dbo].[Names](
	NameId int primary key not null,
	NameType varchar(20) not null,
	BaseText varchar(50) not null
)
go

create table [dbo].[CategoryList](
	CategoryListId int primary key not null,
	CategorySystem varchar(20) not null,
	CategoryId varchar(20) not null,
	CategoryName varchar(20)
)
go

alter table Places
add constraint fk_LocationId foreign key (LocationId)
	references Locations (LocationId),

	constraint fk_ContactId foreign key (ContactId)
	references Contacts (ContactId),

	constraint fk_NameId foreign key (NameId)
	references Names (NameId),

	constraint fk_CategoryListId foreign key (CategoryListId)
	references CategoryList (CategoryListId)
go