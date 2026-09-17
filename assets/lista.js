/* ===== LISTA DE MODELOS: filtros por categoria ===== */
(()=>{
  const grade=document.getElementById('grade');
  if(!grade||typeof MODELOS==='undefined')return;

  const desenha=(filtro)=>{
    const lista = filtro==='todos' ? MODELOS : MODELOS.filter(m=>m.categoria===filtro);
    grade.innerHTML = lista.map(m=>`
      <a class="mcard" href="${m.slug}.html">
        <div class="capa">
          <span class="etq">${m.etiqueta}</span>
          <img loading="lazy" src="${m.foto}" alt="${m.nome}">
        </div>
        <div class="corpo">
          <h3>${m.nome}</h3>
          <div class="med">${m.comprimento} × ${m.largura}</div>
          <div class="mini">
            <span>Prazo <b>${m.prazo}</b></span>
            <span>Volume <b>${m.volume}</b></span>
          </div>
        </div>
      </a>`).join('');
    if(!lista.length) grade.innerHTML='<p style="color:#7a86a3">Nenhum modelo nesta categoria ainda.</p>';
  };
  desenha('todos');
  document.getElementById('filtros').addEventListener('click',e=>{
    const b=e.target.closest('.fbtn'); if(!b)return;
    document.querySelectorAll('.fbtn').forEach(x=>x.classList.remove('on'));
    b.classList.add('on'); desenha(b.dataset.f);
  });
})();
