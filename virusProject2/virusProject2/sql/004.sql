--近一天省份
CREATE VIEW view_day AS SELECT
province,
sum( casesAdd ) casesSum,
sum( recoveredAdd ) recoveredSum,
sum( deathAdd ) deathSum
FROM
	table3
WHERE
	datediff( CURRENT_DATE (), date )<= 0
GROUP BY
	province
--近一周省份
CREATE VIEW view_week AS SELECT
province,
sum( casesAdd ) casesSum,
sum( recoveredAdd ) recoveredSum,
sum( deathAdd ) deathSum
FROM
	table3
WHERE
	datediff( CURRENT_DATE (), date )<= 6
GROUP BY
	province
--近两周省份
CREATE VIEW view_two_week AS SELECT
province,
sum( casesAdd ) casesSum,
sum( recoveredAdd ) recoveredSum,
sum( deathAdd ) deathSum
FROM
	table3
WHERE
	datediff( CURRENT_DATE (), date )<= 13
GROUP BY
	province
--近一月省份
CREATE VIEW view_month AS SELECT
province,
sum( casesAdd ) casesSum,
sum( recoveredAdd ) recoveredSum,
sum( deathAdd ) deathSum
FROM
	table3
WHERE
	datediff( CURRENT_DATE (), date )<= 29
GROUP BY
	province
--累计省份
CREATE VIEW view_sum AS SELECT
`province`,
`cases` casesSum,
`recovered` recoveredSum,
`death` deathSum
FROM
	table2
WHERE
	date = CURRENT_DATE ()
GROUP BY
	province
--近两周全国每日新增
CREATE VIEW view_two_week_country AS SELECT
date,
sum( casesAdd ) casesSum,
sum( recoveredAdd ) recoveredSum,
sum( deathAdd ) deathSum
FROM
	table3
WHERE
	datediff( CURRENT_DATE (), date )<= 13
GROUP BY
	date
--近一月全国每日新增
CREATE VIEW view_month_country AS SELECT
date,
sum( casesAdd ) casesSum,
sum( recoveredAdd ) recoveredSum,
sum( deathAdd ) deathSum
FROM
	table3
WHERE
	datediff( CURRENT_DATE (), date )<= 29
GROUP BY
	date
--近两月上海新增
CREATE VIEW view_two_month_shanghai AS SELECT
date,
province,
casesAdd casesSum,
recoveredAdd recoveredSum,
deathAdd deathSum
FROM
	table3
WHERE
	datediff( CURRENT_DATE (), date )<= 59
	and province = '上海'
--近一月上海新增
CREATE VIEW view_month_shanghai AS SELECT
date,
province,
casesAdd casesSum,
recoveredAdd recoveredSum,
deathAdd deathSum
FROM
	table3
WHERE
	datediff( CURRENT_DATE (), date )<= 29
	and province = '上海'

--近一月全国各省新增
CREATE VIEW view_month_table3 AS SELECT
*
FROM
	table3
WHERE
	datediff( CURRENT_DATE (), date )<= 29
