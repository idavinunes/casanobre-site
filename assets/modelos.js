/* ============================================================
   MODELOS — fonte única de dados
   Para adicionar um modelo: copie um bloco, troque os valores.
   A página /modelos/ e as páginas de detalhe leem daqui.
   ============================================================ */
window.MODELOS = [
  {
    slug: "modelo-a",
    nome: "Nome do Modelo A",
    categoria: "fibra",           // fibra | alvenaria | spa
    etiqueta: "Fibra",
    foto: "../midia/slide-tropical.jpg",
    galeria: ["../midia/slide-tropical.jpg","../midia/quintal.jpg","../midia/slide-hotel.jpg","../midia/slide-agua.jpg"],
    resumo: "Descrição curta do modelo — onde ele se encaixa melhor e para que tipo de quintal foi pensado.",
    comprimento: "0,00 m",
    largura: "0,00 m",
    profundidade: "0,00 m a 0,00 m",
    volume: "00.000 L",
    area: "00,00 m²",
    prazo: "00 dias",
    garantia: "00 anos no casco",
    borda: "A definir",
    opcionais: ["Prainha","Iluminação LED","Hidromassagem","Cascata","Aquecimento","Deck em volta"]
  },
  {
    slug: "modelo-b",
    nome: "Nome do Modelo B",
    categoria: "fibra",
    etiqueta: "Fibra",
    foto: "../midia/quintal.jpg",
    galeria: ["../midia/quintal.jpg","../midia/slide-palmeiras.jpg","../midia/slide-agua.jpg","../midia/slide-hotel.jpg"],
    resumo: "Descrição curta do modelo — onde ele se encaixa melhor e para que tipo de quintal foi pensado.",
    comprimento: "0,00 m", largura: "0,00 m", profundidade: "0,00 m a 0,00 m",
    volume: "00.000 L", area: "00,00 m²", prazo: "00 dias", garantia: "00 anos no casco",
    borda: "A definir",
    opcionais: ["Prainha","Iluminação LED","Cascata","Deck em volta"]
  },
  {
    slug: "modelo-c",
    nome: "Nome do Modelo C",
    categoria: "fibra",
    etiqueta: "Fibra",
    foto: "../midia/slide-hotel.jpg",
    galeria: ["../midia/slide-hotel.jpg","../midia/slide-tropical.jpg","../midia/quintal.jpg","../midia/slide-palmeiras.jpg"],
    resumo: "Descrição curta do modelo — onde ele se encaixa melhor e para que tipo de quintal foi pensado.",
    comprimento: "0,00 m", largura: "0,00 m", profundidade: "0,00 m a 0,00 m",
    volume: "00.000 L", area: "00,00 m²", prazo: "00 dias", garantia: "00 anos no casco",
    borda: "A definir",
    opcionais: ["Iluminação LED","Hidromassagem","Aquecimento"]
  },
  {
    slug: "spa-redondo",
    nome: "Spa / Banheira",
    categoria: "spa",
    etiqueta: "Spa",
    foto: "../midia/slide-gramado.jpg",
    galeria: ["../midia/slide-gramado.jpg","../midia/slide-agua.jpg","../midia/slide-palmeiras.jpg","../midia/quintal.jpg"],
    resumo: "Spa compacto para área de lazer ou varanda — pode ser instalado enterrado ou apoiado.",
    comprimento: "0,00 m", largura: "0,00 m", profundidade: "0,00 m",
    volume: "0.000 L", area: "0,00 m²", prazo: "00 dias", garantia: "00 anos",
    borda: "A definir",
    opcionais: ["Hidromassagem","Aquecimento","Iluminação LED","Capa térmica"]
  },
  {
    slug: "sob-medida",
    nome: "Projeto sob medida",
    categoria: "alvenaria",
    etiqueta: "Alvenaria",
    foto: "../midia/slide-palmeiras.jpg",
    galeria: ["../midia/slide-palmeiras.jpg","../midia/slide-hotel.jpg","../midia/slide-tropical.jpg","../midia/quintal.jpg"],
    resumo: "Piscina em alvenaria construída no formato do seu terreno — sem limite de medida ou desenho.",
    comprimento: "Sob medida", largura: "Sob medida", profundidade: "Sob medida",
    volume: "Conforme projeto", area: "Conforme projeto", prazo: "00 a 00 dias",
    garantia: "00 anos", borda: "Infinita, prainha ou tradicional",
    opcionais: ["Borda infinita","Prainha","Raia","Iluminação LED","Hidromassagem","Aquecimento","Cascata"]
  }
];
