/* ===== COMUM A TODAS AS PAGINAS ===== */
(()=>{
  // barra ganha fundo branco ao rolar (na home ela comeca transparente)
  const barra=document.getElementById('barra');
  if(barra&&!barra.classList.contains('solida')){
    const olha=()=>barra.classList.toggle('fixa',scrollY>60);
    addEventListener('scroll',olha,{passive:true}); olha();
  }

  // revela os blocos .rev quando entram na tela
  const io=new IntersectionObserver(es=>es.forEach(e=>{
    if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}
  }),{threshold:.14,rootMargin:'0px 0px -60px 0px'});
  document.querySelectorAll('.rev').forEach(e=>{
    // blindagem: se o bloco ja esta acima da viewport (recarregou no meio da
    // pagina, veio de uma ancora), ele nunca vai "entrar" na tela — entao
    // revela na hora. Sem isso o conteudo fica invisivel e sem erro nenhum.
    if(e.getBoundingClientRect().bottom<0){e.classList.add('on');return}
    io.observe(e);
  });

  // menu do celular
  const bt=document.getElementById('menuBtn'), nav=document.querySelector('.nav');
  if(bt&&nav){
    bt.onclick=()=>{
      const abriu=nav.classList.toggle('aberto');
      bt.classList.toggle('x',abriu);
      bt.setAttribute('aria-expanded',abriu?'true':'false');
    };
    nav.addEventListener('click',e=>{
      if(e.target.tagName==='A'){nav.classList.remove('aberto');bt.classList.remove('x');
        bt.setAttribute('aria-expanded','false');}
    });
  }
})();
