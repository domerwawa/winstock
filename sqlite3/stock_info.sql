drop table stock_info;
CREATE TABLE stock_info
(
  stock_code character(6) NOT NULL,
  stock_name character varying(50),
  star_level Integer,
  --所属行业
  industrial_category character(100),
  --总市值
  total_market_value decimal,
  --总股本
  general_capital decimal,
  --流通股本
  circulation_stock decimal,
  insert_time timestamp without time zone,
  update_time timestamp without time zone,
  CONSTRAINT stock_info_idx1 PRIMARY KEY (stock_code)
)
WITH (
  OIDS = FALSE
)
;
ALTER TABLE stock_info
  OWNER TO adams;
