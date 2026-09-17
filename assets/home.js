/* ===== HOME: fundo do hero + carrossel ===== */

/* --- FUNDO DO HERO: video do YouTube OU fotos em transicao --- */
(()=>{
  const cx=document.getElementById('bgVideo');
  if(!cx)return;
  const id=(cx.dataset.video||'').trim();
  const ini=(cx.dataset.inicio||'').trim();   // segundo em que o trecho comeca
  const fim=(cx.dataset.fim||'').trim();      // segundo em que o trecho termina
  const fotos=[...document.querySelectorAll('.hero .foto')];

  const v=document.querySelector('.hero video');
  if(v){v.addEventListener('error',()=>v.style.display='none');if(!v.currentSrc)v.style.display='none';}

  if(id){
    // tem video: monta o iframe (mesma tecnica da Cristal Pool) e esconde as fotos
    const p=new URLSearchParams({autoplay:'1',mute:'1',loop:'1',playlist:id,controls:'0',
      showinfo:'0',rel:'0',modestbranding:'1',playsinline:'1',disablekb:'1',iv_load_policy:'3'});
    // corta um trecho do video (o Cristal Pool usa 73s a 130s do video deles)
    if(ini) p.set('start',ini);
    if(fim) p.set('end',fim);
    cx.innerHTML=`<iframe src="https://www.youtube-nocookie.com/embed/${id}?${p}" `+
      `allow="autoplay; encrypted-media" allowfullscreen title="Vídeo de fundo"></iframe>`;
    fotos.forEach(f=>f.style.display='none');
    return;
  }

  // sem video: as fotos giram com fade lento.
  // a 1a foto e visivel por CSS puro; 'saiu' so entra quando a rotacao comeca.
  if(fotos.length<2)return;
  let i=0;
  setInterval(()=>{
    fotos[i].classList.remove('mostra');
    if(i===0) fotos[0].classList.add('saiu');
    i=(i+1)%fotos.length;
    fotos[i].classList.add('mostra');
    if(i===0) fotos[0].classList.remove('saiu');
  },6500);
})();

/* --- CARROSSEL --- */
(()=>{
  const trilho=document.getElementById('trilho');
  if(!trilho)return;
  const slides=[...trilho.children];
  const pontos=document.getElementById('pontos');
  const prog=document.getElementById('barraProg');
  const DUR=6000;
  let i=0,timer=null,t0=0,raf=null;

  slides.forEach((_,k)=>{
    const b=document.createElement('button');
    b.className='pt'+(k===0?' on':'');
    b.setAttribute('aria-label','Slide '+(k+1));
    b.onclick=()=>{vai(k);reinicia()};
    pontos.appendChild(b);
  });

  function vai(n){
    i=(n+slides.length)%slides.length;
    trilho.style.transform=`translateX(-${i*100}%)`;
    [...pontos.children].forEach((p,k)=>p.classList.toggle('on',k===i));
    slides.forEach((s,k)=>{
      const vd=s.querySelector('video');
      if(!vd)return;
      if(k===i){vd.play().catch(()=>{});}else{vd.pause();vd.currentTime=0;}
    });
  }
  function anima(ts){
    if(!t0)t0=ts;
    const p=Math.min((ts-t0)/DUR,1);
    prog.style.width=(p*100)+'%';
    if(p<1)raf=requestAnimationFrame(anima);
  }
  function reinicia(){
    clearInterval(timer);cancelAnimationFrame(raf);t0=0;prog.style.width='0%';
    raf=requestAnimationFrame(anima);
    timer=setInterval(()=>{vai(i+1);t0=0;cancelAnimationFrame(raf);raf=requestAnimationFrame(anima);},DUR);
  }
  document.getElementById('prox').onclick=()=>{vai(i+1);reinicia()};
  document.getElementById('ant').onclick=()=>{vai(i-1);reinicia()};

  // pausa quando o mouse esta em cima
  const car=document.getElementById('carrossel');
  car.addEventListener('mouseenter',()=>{clearInterval(timer);cancelAnimationFrame(raf)});
  car.addEventListener('mouseleave',reinicia);

  // arrastar no celular
  let x0=null;
  car.addEventListener('touchstart',e=>x0=e.touches[0].clientX,{passive:true});
  car.addEventListener('touchend',e=>{
    if(x0===null)return;
    const d=e.changedTouches[0].clientX-x0;
    if(Math.abs(d)>45){vai(d<0?i+1:i-1);reinicia()}
    x0=null;
  },{passive:true});

  // so roda quando o carrossel esta visivel
  new IntersectionObserver(es=>es.forEach(e=>{
    if(e.isIntersecting){vai(i);reinicia()}else{clearInterval(timer);cancelAnimationFrame(raf)}
  }),{threshold:.3}).observe(car);
})();
