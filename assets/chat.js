/* ===== WEB CHAT (demo de fluxo) ===== */
(()=>{
  const btn=document.getElementById('chatBtn'),jan=document.getElementById('chatJan'),
        x=document.getElementById('chatX'),corpo=document.getElementById('chatCorpo'),
        form=document.getElementById('chatForm'),input=document.getElementById('chatInput');
  let iniciado=false;

  const add=(txt,quem='bot')=>{
    const d=document.createElement('div');
    d.className='msg '+quem;d.textContent=txt;
    corpo.appendChild(d);corpo.scrollTop=corpo.scrollHeight;return d;
  };
  const chips=(lista)=>{
    const w=document.createElement('div');w.className='chips';
    lista.forEach(t=>{
      const c=document.createElement('button');
      c.className='chip';c.type='button';c.textContent=t;
      c.onclick=()=>{w.remove();add(t,'eu');responde(t)};
      w.appendChild(c);
    });
    corpo.appendChild(w);corpo.scrollTop=corpo.scrollHeight;
  };
  const digitando=()=>{
    const d=document.createElement('div');
    d.className='digitando';d.innerHTML='<i></i><i></i><i></i>';
    corpo.appendChild(d);corpo.scrollTop=corpo.scrollHeight;return d;
  };
  const bot=(txt,depois,ms=1100)=>{
    const t=digitando();
    setTimeout(()=>{t.remove();add(txt);depois&&depois()},ms);
  };
  function responde(){
    bot('Perfeito. Para eu já adiantar o orçamento: qual a medida aproximada do espaço? (ex.: 8 × 4 m)',()=>{},1300);
  }
  function abrir(){
    jan.classList.add('aberto');
    if(!iniciado){
      iniciado=true;
      bot('Oi! Aqui é a Casa Nobre 👋',()=>{
        bot('Quer ver modelos de piscina ou já tem um projeto em mente?',()=>{
          chips(['Ver modelos','Quero orçamento','Tenho um projeto','Falar com atendente']);
        },1200);
      },700);
    }
    setTimeout(()=>input.focus(),380);
  }
  btn.onclick=()=>jan.classList.contains('aberto')?jan.classList.remove('aberto'):abrir();
  x.onclick=()=>jan.classList.remove('aberto');
  // todos os CTAs do site abrem o chat
  document.querySelectorAll('[data-chat]').forEach(a=>{
    a.addEventListener('click',e=>{e.preventDefault();abrir()});
  });
  form.onsubmit=e=>{
    e.preventDefault();
    const t=input.value.trim();if(!t)return;
    add(t,'eu');input.value='';
    bot('Recebi! Um atendente responde em instantes. Se preferir, deixe seu telefone que retornamos.',()=>{},1200);
  };
})();
