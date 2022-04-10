CREATE TABLE IF NOT EXISTS products_prices_timelapse (
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY (
        INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1
    ),
    id_product uuid NOT NULL,
    price integer NOT NULL,
    date timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT products_prices_timelapse_pkey PRIMARY KEY (id),
    CONSTRAINT id_product FOREIGN KEY (id_product) REFERENCES public.products (id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION
)