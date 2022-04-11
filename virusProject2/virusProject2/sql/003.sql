--汉字与拼音转换函数
CREATE DEFINER=`root`@`localhost` FUNCTION `get_province_character`(province_pinyin varchar(255)) RETURNS varchar(255) CHARSET utf8mb3 COLLATE utf8_bin
    DETERMINISTIC
BEGIN
	DECLARE p_char varchar(255) default 'ok';
	set p_char = (select chinese_character from province_contranst where chinese_pinyin=province_pinyin);
	RETURN p_char;
RETURN 1;
END;
--sql计算每日新增存储过程
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_province_add`(in a_date date,in a_province varchar(255),out a int,out b int,out c int)
    DETERMINISTIC
BEGIN
	declare aa int default 0;
    declare aa2 int default 0;
    declare bb int default 0;
    declare bb2 int default 0;
    declare cc int default 0;
    declare cc2 int default 0;
    declare b_date date default '2022-04-04';
    set b_date = date_sub(a_date,interval 1 day);
	set aa = (select cases from table2 where province=a_province and `date`=a_date);
    set aa2 = (select cases from table2 where province=a_province and `date`=b_date);
    set bb = (select recovered from table2 where province=a_province and `date`=a_date);
    set bb2 = (select recovered from table2 where province=a_province and `date`=b_date);
    set cc = (select death from table2 where province=a_province and `date`=a_date);
    set cc2 = (select death from table2 where province=a_province and `date`=b_date);
	if (isnull(aa2)) then set aa2 = 0; end if;
    if (isnull(bb2)) then set bb2 = 0; end if;
    if (isnull(cc2)) then set cc2 = 0; end if;
    set a = aa - aa2;
    set b = bb - bb2;
    set c = cc - cc2;
END
--第一次向每日新增表填充数据存储过程
CREATE DEFINER=`root`@`localhost` PROCEDURE `gen_province_add`()
    DETERMINISTIC
BEGIN
declare a int default 0;
declare b int default 0;
declare c int default 0;
declare a_date date default '2022-04-03';
declare a_province varchar(255) default '安徽';
declare a_cursor cursor for select `date`,`province` from table2;
open a_cursor;
while(!isnull(a_date)) do
	fetch next from a_cursor into a_date,a_province;
    call virusproject.get_province_add(a_date, a_province, a, b, c);
    insert into table3(`date`,`province`,`casesAdd`,`recoveredAdd`,`deathAdd`) values (a_date,a_province,abs(a),abs(b),abs(c));
end	while;
close a_cursor;
END
--每日向每日新增表填充数据存储过程
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_now_province_add`()
    DETERMINISTIC
BEGIN
declare a int default 0;
declare b int default 0;
declare c int default 0;
declare a_date date default current_date();
declare a_province varchar(255) default '安徽';
declare b_cursor cursor for select `date`,`province` from table2 where `date`=a_date;
open b_cursor;
while(!isnull(a_date)) do
	fetch next from b_cursor into a_date,a_province;
    call virusproject.get_province_add(a_date, a_province, a, b, c);
	select a_date,a_province,abs(a),abs(b),abs(c);
    insert into table3(`date`,`province`,`casesAdd`,`recoveredAdd`,`deathAdd`) values (a_date,a_province,abs(a),abs(b),abs(c));
end	while;
close b_cursor;
END
--插入指定日期省份新增存储过程
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_date_data`(in a_date date)
BEGIN
INSERT INTO table2 ( `date`, province, cases, recovered, death ) SELECT
`date`,
`province`,
`cases`,
`recovered`,
`death`
FROM
	ds_sp_table
WHERE
	date = DATE( a_date );
--进行汉语拼音与汉语字符转换
UPDATE table2 A,
province_contranst B
SET A.province = B.chinese_character
WHERE
	A.province = B.chinese_pinyin;
END