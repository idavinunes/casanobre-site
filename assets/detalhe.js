/* ===== DETALHE DO MODELO: galeria ===== */
(()=>{
  const minis=document.getElementById('gminis'), foto=document.getElementById('gfoto');
  if(!minis||!foto)return;
  minis.addEventListener('click',e=>{
    const t=e.target.closest('.gmini'); if(!t)return;
    foto.src=t.dataset.src;
    minis.querySelectorAll('.gmini').forEach(x=>x.classList.remove('on'));
    t.classList.add('on');
  });
})();
