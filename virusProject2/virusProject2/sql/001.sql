--创建数据库
create database virusProject character set utf8;
alter database virusProject collate utf8_bin;
use virusproject;
--创建各个数据基础表
create table if not exists `bd_table`(
	`date` date not null,
	`confirmAdd` int,
	`mainlandAdd` int,
	`overseaAdd` int,
	`asymptomaticAdd` int,
	`confirmNow` int,
	`mainlandNow` int,
	`overseaNow` int,
	`asymptomaticNow` int,
	`confirmSum` int,
	`overseaSum` int,
	`cureSum` int,
	`deathSum` int,
	primary key (date)
);
create table if not exists `bd_table2`(
	`date` date not null,
	`province` varchar(255) not null,
	`city` varchar(255) not null,
	`confirmAdd` int,
	`mainlandAdd` int,
	`asymptomaticAdd` int,
	`confirmSum` int,
	`cureSum` int,
	`deathSum` int,
	primary key (date,province,city)
);
create table if not exists `bd_table3`(
	`date` date not null,
	`province` varchar(255) not null,
	`confirmAdd` int,
	`confirmSum` int,
	`cureSum` int,
	`deathSum` int,
	primary key (date,province)
);
create table if not exists `ds_table`(
	`date` date not null,
	`cases` int,
	`recovered` int,
	`death` int,
	primary key (date)
);
create table if not exists `ds_table2`(
	`date` date not null,
	`province` varchar(255) not null,
	`cases` int,
	`recovered` int,
	`death` int,
	primary key (date,province)
);
