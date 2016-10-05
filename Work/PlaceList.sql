create database PlaceList
go
use [PlaceList]
go

create table [dbo].[Places](
	PlaceId varchar(50) not null primary key,
	[TimeStamp] datetime not null,
	LocationId int not null,
	ContactListId varchar(50) not null,
	NameId varchar(50) not null,
	CategoryListId varchar(50) not null	
)
go

create table [dbo].[Locations](
	LocationId int primary key not null,
	AddressId varchar(50) not null,
	GeoPositionId varchar(50) not null
)
go

create table dbo.[Address](
	AddressId varchar(50) primary key not null,
	StreetId varchar(50) not null,
	HouseNumber varchar(6),
	CountryCodeId varchar(50) not null,
	AdminNameId varchar(50) not null,
	PostalCode int
)
go

create table dbo.GeoPositions(
	GeoPositionId varchar(50) primary key not null,
	Latitude float(24) not null,
	Longitude float(24) not null,
	Altitude int
)
go

alter table Locations
add constraint fk_AddressId foreign key (AddressId)
	references [Address] (AddressId),

	constraint fk_GeoPositionId foreign key (GeoPositionId)
	references GeoPositions (GeoPositionId)
go

create table [dbo].[Streets](
	StreetId varchar(50) primary key not null,
	BaseName varchar(50) not null,
	StreetType varchar(20)
)
go

create table [dbo].[CountryCodes](
	CountryCodeId varchar(50) primary key not null,
	CountryCode varchar(3) not null,
	AdminLevel1 varchar(20),
	AdminLevel2 varchar(20),
	AdminLevel3 varchar(20),
	AdminLevel4 varchar(20)
)
go

create table dbo.AdminNames(
	AdminNameId varchar(50) primary key not null,
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

create table [dbo].[ContactList](
	ContactListId varchar(50) primary key not null
)
go

create table [dbo].[Contacts](
	ContactId varchar(50) primary key not null,
	ContactType varchar(20) not null,
	ContactString varchar(50) not null,
	ContactListId varchar(50) not null
)
go
alter table Contacts
add constraint fk_ContactListIdForContacts foreign key (ContactListId)
	references ContactList (ContactListId)
go
create table [dbo].[Names](
	NameId varchar(50) primary key not null,
	NameType varchar(20) not null,
	BaseText varchar(50) not null
)
go

create table [dbo].[Categories](
	CategoryId varchar(50) primary key not null,
	CategorySystem varchar(20) not null,
	Category varchar(20) not null,
	CategoryName varchar(20),
	CategoryListId varchar(50) not null
)
go
create table [dbo].[CategoryList](
	CategoryListId varchar(50) primary key not null,
)
go

alter table Categories
add constraint fk_CategoryListIdForCategories foreign key (CategoryListId)
	references CategoryList (CategoryListId)
go

alter table Places
add constraint fk_LocationId foreign key (LocationId)
	references Locations (LocationId),

	constraint fk_ContactListIdForPlace foreign key (ContactListId)
	references ContactList (ContactListId),

	constraint fk_NameId foreign key (NameId)
	references Names (NameId),

	constraint fk_CategoryListIdForPlace foreign key (CategoryListId)
	references CategoryList (CategoryListId)
go