CREATE TABLE IF NOT EXISTS public.products (
    id uuid NOT NULL,
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    id_category integer NOT NULL,
    id_supermarket integer NOT NULL,
    url character varying(2083) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT products_pkey PRIMARY KEY (id),
    CONSTRAINT id_category FOREIGN KEY (id_category) REFERENCES public.categories (id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION,
    CONSTRAINT id_supermarket FOREIGN KEY (id_supermarket) REFERENCES public.supermarkets (id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION
)