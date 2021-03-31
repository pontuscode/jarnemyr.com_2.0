CREATE TABLE trades(
	id 			INT 		NOT NULL IDENTITY PRIMARY KEY,
	date_time 	DATETIME 	NOT NULL,
	symbol_A 	varchar(10) NOT NULL,
	symbol_B 	varchar(10) NOT NULL,
	symbol_C 	varchar(10) NOT NULL,
	price_BA 	float		NOT NULL,
	price_CB	float		NOT NULL,
	price_CA 	float		NOT NULL,
);
