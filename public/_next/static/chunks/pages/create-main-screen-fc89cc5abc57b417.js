(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[364],{4236:function(e,t,r){(window.__NEXT_P=window.__NEXT_P||[]).push(["/create-main-screen",function(){return r(5603)}])},8865:function(e,t,r){"use strict";r.d(t,{Z:function(){return n}});let n=(0,r(6583).Z)("Check",[["path",{d:"M20 6 9 17l-5-5",key:"1gmf2c"}]])},9531:function(e,t,r){"use strict";r.d(t,{Z:function(){return n}});let n=(0,r(6583).Z)("Facebook",[["path",{d:"M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z",key:"1jg4f8"}]])},734:function(e,t,r){"use strict";r.d(t,{Z:function(){return n}});let n=(0,r(6583).Z)("Instagram",[["rect",{width:"20",height:"20",x:"2",y:"2",rx:"5",ry:"5",key:"2e1cvw"}],["path",{d:"M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z",key:"9exkf1"}],["line",{x1:"17.5",x2:"17.51",y1:"6.5",y2:"6.5",key:"r4j83e"}]])},5603:function(e,t,r){"use strict";r.r(t),r.d(t,{Checkbox_ae2ccbecaeba654b251641112d096bc1:function(){return E},Div_bd4c022a8f796682aa6392e9d4c102e9:function(){return y},Errorboundary_543d5ca6cd46fe23c9ec29b1fa97766a:function(){return v},Fragment_6fbb893c40a9a490bea6744d402199de:function(){return k},Fragment_9017984ada32ffa55f5d2870ebd3c887:function(){return H},Fragment_9106b69258ec2cc4dd613c8021efe1be:function(){return D},Toaster_6e6ebf8d7ce589d59b7d382fb7576edf:function(){return w},default:function(){return A}});var n=r(2729),i=r(5944),o=r(4511),a=r(7294),s=r(8039),c=r(9654),d=r(917),l=r(8865),m=r(9531),p=r(734),h=r(2658),g=r(4712),u=r(3954),f=r(7563),x=r(1664),_=r.n(x),Z=r(9008),b=r.n(Z);function C(){let e=(0,n._)(["\n    0% {\n        opacity: 0;\n    }\n    100% {\n        opacity: 1;\n    }\n"]);return C=function(){return e},e}function w(){let{resolvedColorMode:e}=(0,a.useContext)(s.ColorModeContext);c.refs.__toast=g.Am;let[t,r]=(0,a.useContext)(s.EventLoopContext),n={description:"Check if server is reachable at "+(0,c.getBackendURL)(u.Ks).href,closeButton:!0,duration:12e4,id:"websocket-error"},[o,d]=(0,a.useState)(!1);return(0,a.useEffect)(()=>{r.length>=2?o||g.Am.error("Cannot connect to server: ".concat(r.length>0?r[r.length-1].message:"","."),{...n,onDismiss:()=>d(!0)}):(g.Am.dismiss("websocket-error"),d(!1))},[r]),(0,i.tZ)(g.x7,{closeButton:!1,expand:!0,position:"bottom-right",richColors:!0,theme:e})}function y(){let[e,t]=(0,a.useContext)(s.EventLoopContext);return(0,i.tZ)("div",{css:{position:"fixed",width:"100vw",height:"0"},title:"Connection Error: "+(t.length>0?t[t.length-1].message:""),children:(0,i.tZ)(H,{})})}let B=(0,d.keyframes)(C());function E(){let[e,t]=(0,a.useContext)(s.EventLoopContext),r=(0,a.useCallback)(t=>e([(0,c.Event)("reflex___state____state.mena_cumples___states___form_state____form_base_state.update_field",{field:"conditions_acepted",value:t},{})],[t],{}),[e,c.Event]);return(0,i.tZ)(f.Checkbox,{color:"violet",onCheckedChange:r,required:!0,size:"2"})}function k(){let e=(0,a.useContext)(s.StateContexts.reflex___state____state__mena_cumples___states___form_state____form_base_state);return(0,i.tZ)(a.Fragment,{children:(0,c.isTrue)(e.conditions_acepted)?(0,i.tZ)(a.Fragment,{children:(0,i.tZ)(f.Link,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,i.tZ)(_(),{href:"/pack_selection",passHref:!0,children:(0,i.BX)(f.Box,{css:{padding:"2rem",boxShadow:"0px 4px 6px rgba(0, 0, 0, 0.1)",borderRadius:"0.5rem",backgroundColor:"white","&:hover":{textDecoration:"none"}},children:[(0,i.tZ)("img",{alt:"seleccion del pack",css:{borderRadius:"0.5rem"},src:"/pedidos_image.webp"}),(0,i.tZ)(f.Heading,{align:"center",as:"h2",css:{marginTop:"1.5rem",fontWeight:"700",marginBottom:"1rem",fontSize:"1.5rem",lineHeight:"2rem",color:"#7C3AED"},children:"\xa1 Haz tu pedido !"}),(0,i.tZ)(f.Text,{as:"p",css:{marginBottom:"2rem",color:"#6D28D9",fontSize:"1.25rem",lineHeight:"1.75rem"},children:"Debe aceptar condiciones y seleccione pack."})]})})})}):(0,i.tZ)(a.Fragment,{children:(0,i.BX)(f.Box,{css:{padding:"2rem",boxShadow:"0px 4px 6px rgba(0, 0, 0, 0.1)",borderRadius:"0.5rem",backgroundColor:"#f0f0f0",cursor:"not-allowed",opacity:.6},children:[(0,i.tZ)("img",{alt:"seleccion del pack",css:{borderRadius:"0.5rem",opacity:.6},src:"/pedidos_image.webp"}),(0,i.tZ)(f.Heading,{align:"center",as:"h2",css:{marginTop:"1.5rem",fontWeight:"700",marginBottom:"1rem",fontSize:"1.5rem",lineHeight:"2rem",color:"#7C3AED"},children:"\xa1 Haz tu pedido !"}),(0,i.tZ)(f.Text,{as:"p",css:{marginBottom:"2rem",color:"#6D28D9",fontSize:"1.25rem",lineHeight:"1.75rem"},children:"Debe aceptar condiciones y seleccione pack."})]})})})}function v(){let[e,t]=(0,a.useContext)(s.EventLoopContext),r=(0,a.useCallback)((t,r)=>e([(0,c.Event)("reflex___state____state.reflex___state____frontend_event_exception_state.handle_frontend_exception",{stack:t.stack,component_stack:r.componentStack},{})],[t,r],{}),[e,c.Event]);return(0,i.BX)(o.SV,{fallbackRender:t=>(0,d.jsx)("div",{css:{height:"100%",width:"100%",position:"absolute",display:"flex",alignItems:"center",justifyContent:"center"}},(0,d.jsx)("div",{css:{display:"flex",flexDirection:"column",gap:"1rem"}},(0,d.jsx)("div",{css:{display:"flex",flexDirection:"column",gap:"1rem",maxWidth:"50ch",border:"1px solid #888888",borderRadius:"0.25rem",padding:"1rem"}},(0,d.jsx)("h2",{css:{fontSize:"1.25rem",fontWeight:"bold"}},(0,d.jsx)(a.Fragment,{},"An error occurred while rendering this page.")),(0,d.jsx)("p",{css:{opacity:"0.75"}},(0,d.jsx)(a.Fragment,{},"This is an error with the application itself.")),(0,d.jsx)("details",{},(0,d.jsx)("summary",{css:{padding:"0.5rem"}},(0,d.jsx)(a.Fragment,{},"Error message")),(0,d.jsx)("div",{css:{width:"100%",maxHeight:"50vh",overflow:"auto",background:"#000",color:"#fff",borderRadius:"0.25rem"}},(0,d.jsx)("div",{css:{padding:"0.5rem",width:"fit-content"}},(0,d.jsx)("pre",{},(0,d.jsx)(a.Fragment,{},t.error.stack)))),(0,d.jsx)("button",{css:{padding:"0.35rem 0.75rem",margin:"0.5rem",background:"#fff",color:"#000",border:"1px solid #000",borderRadius:"0.25rem",fontWeight:"bold"},onClick:function(){for(var r=arguments.length,n=Array(r),i=0;i<r;i++)n[i]=arguments[i];return e([(0,c.Event)("_call_function",{function:()=>navigator.clipboard.writeText(t.error.stack)},{})],n,{})}},(0,d.jsx)(a.Fragment,{},"Copy")))),(0,d.jsx)("hr",{css:{borderColor:"currentColor",opacity:"0.25"}}),(0,d.jsx)("a",{href:"https://reflex.dev"},(0,d.jsx)("div",{css:{display:"flex",alignItems:"baseline",justifyContent:"center",fontFamily:"monospace","--default-font-family":"monospace",gap:"0.5rem"}},(0,d.jsx)(a.Fragment,{},"Built with "),(0,d.jsx)("svg",{css:{viewBox:"0 0 56 12",fill:"currentColor"},height:"12",width:"56",xmlns:"http://www.w3.org/2000/svg"},(0,d.jsx)("path",{d:"M0 11.5999V0.399902H8.96V4.8799H6.72V2.6399H2.24V4.8799H6.72V7.1199H2.24V11.5999H0ZM6.72 11.5999V7.1199H8.96V11.5999H6.72Z"}),(0,d.jsx)("path",{d:"M11.2 11.5999V0.399902H17.92V2.6399H13.44V4.8799H17.92V7.1199H13.44V9.3599H17.92V11.5999H11.2Z"}),(0,d.jsx)("path",{d:"M20.16 11.5999V0.399902H26.88V2.6399H22.4V4.8799H26.88V7.1199H22.4V11.5999H20.16Z"}),(0,d.jsx)("path",{d:"M29.12 11.5999V0.399902H31.36V9.3599H35.84V11.5999H29.12Z"}),(0,d.jsx)("path",{d:"M38.08 11.5999V0.399902H44.8V2.6399H40.32V4.8799H44.8V7.1199H40.32V9.3599H44.8V11.5999H38.08Z"}),(0,d.jsx)("path",{d:"M47.04 4.8799V0.399902H49.28V4.8799H47.04ZM53.76 4.8799V0.399902H56V4.8799H53.76ZM49.28 7.1199V4.8799H53.76V7.1199H49.28ZM47.04 11.5999V7.1199H49.28V11.5999H47.04ZM53.76 11.5999V7.1199H56V11.5999H53.76Z"})))))),onError:r,children:[(0,i.BX)(a.Fragment,{children:[(0,i.tZ)(y,{}),(0,i.tZ)(w,{})]}),(0,i.BX)(a.Fragment,{children:[(0,i.tZ)("link",{href:"https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",rel:"stylesheet"}),(0,i.tZ)("style",{suppressHydrationWarning:!0,children:"\n        @font-face {\n            font-family: 'LucideIcons';\n            src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');\n        }\n    "}),(0,i.BX)(f.Box,{css:{backgroundColor:"#FDF2F8"},children:[(0,i.tZ)(f.Box,{className:"bg-gradient-to-r from-pink-200 to-pink-300 via-purple-200",css:{padding:"1rem"},children:(0,i.tZ)(f.Flex,{css:{"@media screen and (min-width: 640px)":{"max-width":"640px"},"@media screen and (min-width: 768px)":{"max-width":"768px"},"@media screen and (min-width: 1024px)":{"max-width":"1024px"},"@media screen and (min-width: 1280px)":{"max-width":"1280px"},"@media screen and (min-width: 1536px)":{"max-width":"1536px"},width:"100%",display:"flex",alignItems:"center",justifyContent:"space-between",marginLeft:"auto",marginRight:"auto"},children:(0,i.tZ)("img",{css:{height:"auto",width:"200px"},src:"/cumpleMena.png"})})}),(0,i.BX)(f.Box,{css:{"@media screen and (min-width: 640px)":{"max-width":"640px"},"@media screen and (min-width: 768px)":{"max-width":"768px"},"@media screen and (min-width: 1024px)":{"max-width":"1024px"},"@media screen and (min-width: 1280px)":{"max-width":"1280px"},"@media screen and (min-width: 1536px)":{"max-width":"1536px"},width:"100%",marginTop:"2rem",marginLeft:"auto",marginRight:"auto"},children:[(0,i.BX)(f.Box,{css:{textAlign:"center"},children:[(0,i.tZ)(f.Heading,{align:"center",as:"h2",css:{marginTop:"1.5rem",fontWeight:"700",marginBottom:"1rem",fontSize:"2.25rem",lineHeight:"2.5rem",color:"#7C3AED"},children:"\xbf Quieres celebrar un cumplea\xf1os ?"}),(0,i.tZ)(f.Text,{as:"p",css:{marginBottom:"2rem",color:"#6D28D9",fontSize:"1.25rem",lineHeight:"1.75rem"},children:"Debe aceptar las condiciones antes de consultar disponibilidad o realizar su pedido."}),(0,i.BX)(f.Box,{css:{backgroundColor:"#EDE9FE",marginTop:"2rem",marginBottom:"2rem",padding:"1.5rem",borderRadius:"0.5rem"},children:[(0,i.tZ)(f.Heading,{align:"left",as:"h2",css:{marginTop:"1.5rem",fontWeight:"700",marginBottom:"1rem",fontSize:"1.875rem",lineHeight:"2.25rem",color:"#7C3AED"},children:"\xa1 CONDICIONES !"}),(0,i.BX)("ul",{css:{direction:"column",listStyleType:"none",gap:"1rem",display:"grid","@media screen and (min-width: 0px)":{gridTemplateColumns:"repeat(1, minmax(0, 1fr))"},"@media screen and (min-width: 768px)":{gridTemplateColumns:"repeat(2, minmax(0, 1fr))"}},children:[(0,i.BX)("li",{css:{display:"flex",alignItems:"center"},children:[(0,i.tZ)(l.Z,{css:{color:"#7C3AED",marginRight:"0.5rem"}}),(0,i.tZ)("span",{css:{color:"#7C3AED"},children:"Est\xe1 prohibida bebida o comida de fuera del establecimiento."})]}),(0,i.BX)("li",{css:{display:"flex",alignItems:"center"},children:[(0,i.tZ)(l.Z,{css:{color:"#7C3AED",marginRight:"0.5rem"}}),(0,i.tZ)("span",{css:{color:"#7C3AED"},children:"La edad m\xe1xima para elegir los packs de cumples es de 12 a\xf1os."})]}),(0,i.BX)("li",{css:{display:"flex",alignItems:"center"},children:[(0,i.tZ)(l.Z,{css:{color:"#7C3AED",marginRight:"0.5rem"}}),(0,i.tZ)("span",{css:{color:"#7C3AED"},children:"Las mesas y sillas se montar\xe1n dependiendo del pack que elija."})]}),(0,i.BX)("li",{css:{display:"flex",alignItems:"center"},children:[(0,i.tZ)(l.Z,{css:{color:"#7C3AED",marginRight:"0.5rem"}}),(0,i.tZ)("span",{css:{color:"#7C3AED"},children:"La duraci\xf3n m\xe1xima del cumplea\xf1os es de 2 horas y media."})]}),(0,i.BX)("li",{css:{display:"flex",alignItems:"center"},children:[(0,i.tZ)(l.Z,{css:{color:"#7C3AED",marginRight:"0.5rem"}}),(0,i.tZ)("span",{css:{color:"#7C3AED"},children:"Las chucher\xedas se permiten en cucuruchos (mesas de chuches no)"})]}),(0,i.BX)("li",{css:{display:"flex",alignItems:"center"},children:[(0,i.tZ)(l.Z,{css:{color:"#7C3AED",marginRight:"0.5rem"}}),(0,i.tZ)("span",{css:{color:"#7C3AED"},children:"Los 50€ de fianza son no reembolsables en caso de cancelaci\xf3n."})]}),(0,i.BX)("li",{css:{display:"flex",alignItems:"center"},children:[(0,i.tZ)(l.Z,{css:{color:"#7C3AED",marginRight:"0.5rem"}}),(0,i.tZ)("span",{css:{color:"#7C3AED"},children:"La celebraci\xf3n puede empezar a m\xe1s tardar a las 19:30h (18:30h desde noviembre)."})]}),(0,i.BX)("li",{css:{display:"flex",alignItems:"center"},children:[(0,i.tZ)(l.Z,{css:{color:"#7C3AED",marginRight:"0.5rem"}}),(0,i.tZ)("span",{css:{color:"#7C3AED"},children:"No colocamos mesas auxiliares aparte, solamente ser\xe1 la mesa del cumplea\xf1os."})]}),(0,i.BX)("li",{css:{display:"flex",alignItems:"center"},children:[(0,i.tZ)(l.Z,{css:{color:"#7C3AED",marginRight:"0.5rem"}}),(0,i.tZ)("span",{css:{color:"#7C3AED"},children:"La decoraci\xf3n depende del espacio \xa1No se puede decorar la pared del supermercado!"})]}),(0,i.BX)("li",{css:{display:"flex",alignItems:"center"},children:[(0,i.tZ)(l.Z,{css:{color:"#7C3AED",marginRight:"0.5rem"}}),(0,i.tZ)("span",{css:{color:"#7C3AED"},children:"La fecha que elijas no podr\xe1 cambiarse m\xe1s adelante."})]}),(0,i.BX)("li",{css:{display:"flex",alignItems:"center"},children:[(0,i.tZ)(l.Z,{css:{color:"#7C3AED",marginRight:"0.5rem"}}),(0,i.tZ)("span",{css:{color:"#7C3AED"},children:"Puedes modificar el pack, seg\xfan disponibilidad, pero no cambiar a un pack menor."})]}),(0,i.BX)("li",{css:{display:"flex",alignItems:"center"},children:[(0,i.tZ)(l.Z,{css:{color:"#7C3AED",marginRight:"0.5rem"}}),(0,i.tZ)("span",{css:{color:"#7C3AED"},children:"Para reservar, primero confirmar n\xba de personas y hora."})]})]}),(0,i.BX)(f.Flex,{align:"center",className:"rx-Stack",css:{marginTop:"40px",marginBottom:"2rem"},direction:"column",gap:"2",children:[(0,i.tZ)(f.Text,{as:"label",size:"2",children:(0,i.BX)(f.Flex,{gap:"2",children:[(0,i.tZ)(E,{}),(0,i.tZ)(f.Text,{as:"p",css:{color:"#e926a8",fontSize:"18px",fontWeight:"bold",marginBottom:"20px"},children:"He le\xeddo y acepto las condiciones. (acepte para poder preguntar por disponibilidad)"})]})}),(0,i.tZ)(f.Text,{as:"p",css:{fontWeight:"bold",color:"#7C3AED"},children:"Se recomienda navegador Chrome o Firefox. Safari de iphone puede dar problemas."})]})]}),(0,i.tZ)(D,{}),(0,i.tZ)(f.Text,{as:"p",css:{marginTop:"2rem",color:"red",fontSize:"1.25rem",lineHeight:"1.75rem",fontWeight:"bold"},children:"A tener en cuenta de que el cumplea\xf1os no est\xe1 confirmado hasta que no se entregue el dep\xf3sito de 50€."})]}),(0,i.BX)(f.Box,{css:{gap:"2rem",display:"grid","@media screen and (min-width: 0px)":{gridTemplateColumns:"repeat(1, minmax(0, 1fr))"},"@media screen and (min-width: 768px)":{gridTemplateColumns:"repeat(2, minmax(0, 1fr))"},marginTop:"4rem",maxWidth:"1000px",marginInlineStart:"auto",marginInlineEnd:"auto"},children:[(0,i.tZ)(a.Fragment,{children:(0,c.isTrue)(!0)?(0,i.tZ)(a.Fragment,{children:(0,i.tZ)(f.Link,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,i.tZ)(_(),{href:"/packs_information",passHref:!0,children:(0,i.BX)(f.Box,{css:{padding:"2rem",boxShadow:"0px 4px 6px rgba(0, 0, 0, 0.1)",borderRadius:"0.5rem",backgroundColor:"white","&:hover":{textDecoration:"none"}},children:[(0,i.tZ)("img",{alt:"Pastel-colored birthday cake with soft pink and purple decorations",css:{borderRadius:"0.5rem"},src:"/packs_info_image.webp"}),(0,i.tZ)(f.Heading,{align:"center",as:"h2",css:{marginTop:"1.5rem",fontWeight:"700",marginBottom:"1rem",fontSize:"1.5rem",lineHeight:"2rem",color:"#7C3AED"},children:"Nuestros Packs de cumples."}),(0,i.tZ)(f.Text,{as:"p",css:{marginBottom:"2rem",color:"#6D28D9",fontSize:"1.25rem",lineHeight:"1.75rem"},children:"Informaci\xf3n de los packs que ofrecemos."})]})})})}):(0,i.tZ)(a.Fragment,{children:(0,i.BX)(f.Box,{css:{padding:"2rem",boxShadow:"0px 4px 6px rgba(0, 0, 0, 0.1)",borderRadius:"0.5rem",backgroundColor:"#f0f0f0",cursor:"not-allowed",opacity:.6},children:[(0,i.tZ)("img",{alt:"Pastel-colored birthday cake with soft pink and purple decorations",css:{borderRadius:"0.5rem",opacity:.6},src:"/packs_info_image.webp"}),(0,i.tZ)(f.Heading,{align:"center",as:"h2",css:{marginTop:"1.5rem",fontWeight:"700",marginBottom:"1rem",fontSize:"1.5rem",lineHeight:"2rem",color:"#7C3AED"},children:"Nuestros Packs de cumples."}),(0,i.tZ)(f.Text,{as:"p",css:{marginBottom:"2rem",color:"#6D28D9",fontSize:"1.25rem",lineHeight:"1.75rem"},children:"Informaci\xf3n de los packs que ofrecemos."})]})})}),(0,i.tZ)(k,{})]}),(0,i.BX)(f.Box,{css:{marginTop:"4rem",textAlign:"center"},children:[(0,i.tZ)(f.Heading,{align:"center",as:"h2",css:{marginTop:"1.5rem",fontWeight:"700",marginBottom:"1rem",fontSize:"1.875rem",lineHeight:"2.25rem",color:"#7C3AED"},children:"\xa1 FELICIDADES !"}),(0,i.tZ)(f.Text,{as:"p",css:{marginBottom:"2rem",color:"#6D28D9",fontSize:"1.25rem",lineHeight:"1.75rem"},children:"\xa1 Gracias por celebrar este d\xeda tan especial con nosotros !"})]})]}),(0,i.tZ)(f.Box,{className:"bg-gradient-to-r from-pink-200 to-pink-300 via-purple-200",css:{marginTop:"4rem",paddingTop:"2rem",paddingBottom:"2rem"},children:(0,i.BX)(f.Box,{css:{"@media screen and (min-width: 640px)":{"max-width":"640px"},"@media screen and (min-width: 768px)":{"max-width":"768px"},"@media screen and (min-width: 1024px)":{"max-width":"1024px"},"@media screen and (min-width: 1280px)":{"max-width":"1280px"},"@media screen and (min-width: 1536px)":{"max-width":"1536px"},width:"100%",marginLeft:"auto",marginRight:"auto",textAlign:"center"},children:[(0,i.tZ)(f.Text,{as:"p",css:{color:"#7C3AED"},children:"\xa9 2024 Developed by Gabriel Visiedo."}),(0,i.BX)(f.Flex,{css:{display:"flex",justifyContent:"center",marginTop:"1rem",columnGap:"1rem"},children:[(0,i.tZ)("a",{css:{transitionDuration:"300ms","&:hover":{color:"#5B21B6"}},href:"https://www.facebook.com/p/Hotel-Mena-Plaza-Nerja-100079174651992/",children:(0,i.tZ)(m.Z,{css:{fontFamily:"LucideIcons","--default-font-family":"LucideIcons",fontSize:"1.5rem",color:"#7C3AED"}})}),(0,i.tZ)("a",{css:{transitionDuration:"300ms","&:hover":{color:"#5B21B6"}},href:"https://www.instagram.com/menaplaza/?hl=es",children:(0,i.tZ)(p.Z,{css:{fontFamily:"LucideIcons","--default-font-family":"LucideIcons",fontSize:"1.5rem",color:"#7C3AED"}})})]})]})})]})]}),(0,i.BX)(b(),{children:[(0,i.tZ)("title",{children:"MenaCumples | Create-Main-Screen"}),(0,i.tZ)("meta",{content:"favicon.ico",property:"og:image"})]})]})}function D(){let e=(0,a.useContext)(s.StateContexts.reflex___state____state__mena_cumples___states___form_state____form_base_state),[t,r]=(0,a.useContext)(s.EventLoopContext);return(0,i.tZ)(a.Fragment,{children:(0,c.isTrue)(e.conditions_acepted)?(0,i.tZ)(a.Fragment,{children:(0,i.tZ)(f.Button,{css:{backgroundColor:"#A78BFA",color:"#ffffff",fontWeight:"700",padding:"2.5rem 2rem",borderRadius:"9999px",transition:"background-color 300ms ease-in-out","&:hover":{backgroundColor:"#8B5CF6"}},onClick:function(){for(var e=arguments.length,r=Array(e),n=0;n<e;n++)r[n]=arguments[n];return t([(0,c.Event)("reflex___state____state.mena_cumples___states___form_state____form_base_state.handle_button_click",{},{})],r,{})},size:"3",children:"PREGUNTAR DISPONIBILIDAD"})}):(0,i.tZ)(a.Fragment,{children:(0,i.tZ)(f.Button,{css:{backgroundColor:"#ebe2f8",color:"#9CA3AF",fontWeight:"700",padding:"2.5rem 2rem",borderRadius:"9999px",cursor:"not-allowed",opacity:.6},children:"PREGUNTAR DISPONIBILIDAD"})})})}function H(){let[e,t]=(0,a.useContext)(s.EventLoopContext);return(0,i.tZ)(a.Fragment,{children:(0,c.isTrue)(t.length>0)?(0,i.tZ)(a.Fragment,{children:(0,i.tZ)(h.Z,{css:{color:"crimson",zIndex:9999,position:"fixed",bottom:"33px",right:"33px",animation:B+" 1s infinite"},size:32})}):(0,i.tZ)(a.Fragment,{})})}function A(){return(0,i.tZ)(v,{})}},4511:function(e,t,r){"use strict";r.d(t,{SV:function(){return a}});var n=r(7294);let i=(0,n.createContext)(null),o={didCatch:!1,error:null};class a extends n.Component{constructor(e){super(e),this.resetErrorBoundary=this.resetErrorBoundary.bind(this),this.state=o}static getDerivedStateFromError(e){return{didCatch:!0,error:e}}resetErrorBoundary(){let{error:e}=this.state;if(null!==e){for(var t,r,n=arguments.length,i=Array(n),a=0;a<n;a++)i[a]=arguments[a];null===(t=(r=this.props).onReset)||void 0===t||t.call(r,{args:i,reason:"imperative-api"}),this.setState(o)}}componentDidCatch(e,t){var r,n;null===(r=(n=this.props).onError)||void 0===r||r.call(n,e,t)}componentDidUpdate(e,t){let{didCatch:r}=this.state,{resetKeys:n}=this.props;if(r&&null!==t.error&&function(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:[],t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:[];return e.length!==t.length||e.some((e,r)=>!Object.is(e,t[r]))}(e.resetKeys,n)){var i,a;null===(i=(a=this.props).onReset)||void 0===i||i.call(a,{next:n,prev:e.resetKeys,reason:"keys"}),this.setState(o)}}render(){let{children:e,fallbackRender:t,FallbackComponent:r,fallback:o}=this.props,{didCatch:a,error:s}=this.state,c=e;if(a){let e={error:s,resetErrorBoundary:this.resetErrorBoundary};if("function"==typeof t)c=t(e);else if(r)c=(0,n.createElement)(r,e);else if(void 0!==o)c=o;else throw s}return(0,n.createElement)(i.Provider,{value:{didCatch:a,error:s,resetErrorBoundary:this.resetErrorBoundary}},c)}}}},function(e){e.O(0,[49,888,774,179],function(){return e(e.s=4236)}),_N_E=e.O()}]);