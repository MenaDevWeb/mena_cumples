(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[586],{762:function(e,t,r){(window.__NEXT_P=window.__NEXT_P||[]).push(["/packs_information",function(){return r(7366)}])},7366:function(e,t,r){"use strict";r.r(t),r.d(t,{Div_bd4c022a8f796682aa6392e9d4c102e9:function(){return B},Errorboundary_8da81bc27ec6621cf86e1dc6839d175c:function(){return Z},Fragment_9017984ada32ffa55f5d2870ebd3c887:function(){return k},Toaster_6e6ebf8d7ce589d59b7d382fb7576edf:function(){return f},default:function(){return _}});var o=r(2729),s=r(5944),a=r(4511),n=r(7294),i=r(8039),c=r(9654),l=r(917),d=r(2658),m=r(4712),p=r(3954),h=r(7563),g=r(9008),x=r.n(g);function u(){let e=(0,o._)(["\n    0% {\n        opacity: 0;\n    }\n    100% {\n        opacity: 1;\n    }\n"]);return u=function(){return e},e}function f(){let{resolvedColorMode:e}=(0,n.useContext)(i.ColorModeContext);c.refs.__toast=m.Am;let[t,r]=(0,n.useContext)(i.EventLoopContext),o={description:"Check if server is reachable at "+(0,c.getBackendURL)(p.Ks).href,closeButton:!0,duration:12e4,id:"websocket-error"},[a,l]=(0,n.useState)(!1);return(0,n.useEffect)(()=>{r.length>=2?a||m.Am.error("Cannot connect to server: ".concat(r.length>0?r[r.length-1].message:"","."),{...o,onDismiss:()=>l(!0)}):(m.Am.dismiss("websocket-error"),l(!1))},[r]),(0,s.tZ)(m.x7,{closeButton:!1,expand:!0,position:"bottom-right",richColors:!0,theme:e})}function B(){let[e,t]=(0,n.useContext)(i.EventLoopContext);return(0,s.tZ)("div",{css:{position:"fixed",width:"100vw",height:"0"},title:"Connection Error: "+(t.length>0?t[t.length-1].message:""),children:(0,s.tZ)(k,{})})}let b=(0,l.keyframes)(u());function Z(){let[e,t]=(0,n.useContext)(i.EventLoopContext),r=(0,n.useCallback)((t,r)=>e([(0,c.Event)("reflex___state____state.reflex___state____frontend_event_exception_state.handle_frontend_exception",{stack:t.stack,component_stack:r.componentStack},{})],[t,r],{}),[e,c.Event]);return(0,s.BX)(a.SV,{fallbackRender:t=>(0,l.jsx)("div",{css:{height:"100%",width:"100%",position:"absolute",display:"flex",alignItems:"center",justifyContent:"center"}},(0,l.jsx)("div",{css:{display:"flex",flexDirection:"column",gap:"1rem"}},(0,l.jsx)("div",{css:{display:"flex",flexDirection:"column",gap:"1rem",maxWidth:"50ch",border:"1px solid #888888",borderRadius:"0.25rem",padding:"1rem"}},(0,l.jsx)("h2",{css:{fontSize:"1.25rem",fontWeight:"bold"}},(0,l.jsx)(n.Fragment,{},"An error occurred while rendering this page.")),(0,l.jsx)("p",{css:{opacity:"0.75"}},(0,l.jsx)(n.Fragment,{},"This is an error with the application itself.")),(0,l.jsx)("details",{},(0,l.jsx)("summary",{css:{padding:"0.5rem"}},(0,l.jsx)(n.Fragment,{},"Error message")),(0,l.jsx)("div",{css:{width:"100%",maxHeight:"50vh",overflow:"auto",background:"#000",color:"#fff",borderRadius:"0.25rem"}},(0,l.jsx)("div",{css:{padding:"0.5rem",width:"fit-content"}},(0,l.jsx)("pre",{},(0,l.jsx)(n.Fragment,{},t.error.stack)))),(0,l.jsx)("button",{css:{padding:"0.35rem 0.75rem",margin:"0.5rem",background:"#fff",color:"#000",border:"1px solid #000",borderRadius:"0.25rem",fontWeight:"bold"},onClick:function(){for(var r=arguments.length,o=Array(r),s=0;s<r;s++)o[s]=arguments[s];return e([(0,c.Event)("_call_function",{function:()=>navigator.clipboard.writeText(t.error.stack)},{})],o,{})}},(0,l.jsx)(n.Fragment,{},"Copy")))),(0,l.jsx)("hr",{css:{borderColor:"currentColor",opacity:"0.25"}}),(0,l.jsx)("a",{href:"https://reflex.dev"},(0,l.jsx)("div",{css:{display:"flex",alignItems:"baseline",justifyContent:"center",fontFamily:"monospace","--default-font-family":"monospace",gap:"0.5rem"}},(0,l.jsx)(n.Fragment,{},"Built with "),(0,l.jsx)("svg",{css:{viewBox:"0 0 56 12",fill:"currentColor"},height:"12",width:"56",xmlns:"http://www.w3.org/2000/svg"},(0,l.jsx)("path",{d:"M0 11.5999V0.399902H8.96V4.8799H6.72V2.6399H2.24V4.8799H6.72V7.1199H2.24V11.5999H0ZM6.72 11.5999V7.1199H8.96V11.5999H6.72Z"}),(0,l.jsx)("path",{d:"M11.2 11.5999V0.399902H17.92V2.6399H13.44V4.8799H17.92V7.1199H13.44V9.3599H17.92V11.5999H11.2Z"}),(0,l.jsx)("path",{d:"M20.16 11.5999V0.399902H26.88V2.6399H22.4V4.8799H26.88V7.1199H22.4V11.5999H20.16Z"}),(0,l.jsx)("path",{d:"M29.12 11.5999V0.399902H31.36V9.3599H35.84V11.5999H29.12Z"}),(0,l.jsx)("path",{d:"M38.08 11.5999V0.399902H44.8V2.6399H40.32V4.8799H44.8V7.1199H40.32V9.3599H44.8V11.5999H38.08Z"}),(0,l.jsx)("path",{d:"M47.04 4.8799V0.399902H49.28V4.8799H47.04ZM53.76 4.8799V0.399902H56V4.8799H53.76ZM49.28 7.1199V4.8799H53.76V7.1199H49.28ZM47.04 11.5999V7.1199H49.28V11.5999H47.04ZM53.76 11.5999V7.1199H56V11.5999H53.76Z"})))))),onError:r,children:[(0,s.BX)(n.Fragment,{children:[(0,s.tZ)(B,{}),(0,s.tZ)(f,{})]}),(0,s.BX)(h.Container,{css:{padding:"1rem",backgroundColor:"#FDF2F8",borderRadius:"10px",alignItems:"center",display:"flex",flexDirection:"column"},size:"3",children:[(0,s.tZ)(h.Box,{css:{display:"flex",justifyContent:"center",alignItems:"center"},children:(0,s.tZ)("img",{css:{width:"500px",marginBottom:"2rem"},src:"/packs_title.png"})}),(0,s.BX)(h.Flex,{align:"start",className:"rx-Stack",direction:"row",gap:"3",children:[(0,s.tZ)(h.Box,{children:(0,s.tZ)("img",{css:{width:"280px",height:"auto"},src:"/pack_15.webp"})}),(0,s.BX)(h.Box,{css:{padding:"1rem",border:"2px solid #BE185D",borderRadius:"10px",marginBottom:"2rem",width:"100%"},children:[(0,s.tZ)(h.Heading,{css:{fontSize:"1.5rem",color:"#8B5CF6",marginBottom:"0.5rem"},children:"Pack para 15 Personas - 90€"}),(0,s.tZ)(h.Text,{as:"p",css:{color:"black",marginBottom:"0.5rem"},children:"• 30 Bocadillos \xf3 15 Sandwiches mixtos (o mitad y mitad)"}),(0,s.tZ)(h.Text,{as:"p",css:{color:"black",marginBottom:"0.5rem"},children:"• Platos: patatas, palomitas, boller\xeda/galletas y frutos secos."}),(0,s.tZ)(h.Text,{as:"p",css:{color:"black",marginBottom:"0.5rem"},children:"• A elegir o combinar: 3 Pizzas \xf3 3 roscas."}),(0,s.tZ)(h.Text,{as:"p",css:{color:"black",marginBottom:"1rem"},children:"• 4 Botellas de refresco."})]})]}),(0,s.BX)(h.Flex,{align:"start",className:"rx-Stack",direction:"row",gap:"3",children:[(0,s.tZ)(h.Box,{children:(0,s.tZ)("img",{css:{width:"280px",height:"auto"},src:"/pack_20_image.webp"})}),(0,s.BX)(h.Box,{css:{padding:"1rem",border:"2px solid #BE185D",borderRadius:"10px",marginBottom:"2rem",width:"100%"},children:[(0,s.tZ)(h.Heading,{css:{fontSize:"1.5rem",color:"#8B5CF6",marginBottom:"0.5rem"},children:"Pack para 20 Personas - 120€"}),(0,s.tZ)(h.Text,{as:"p",css:{color:"black",marginBottom:"0.5rem"},children:"• 40 Bocadillos \xf3 20 Sandwiches mixtos (o mitad y mitad)"}),(0,s.tZ)(h.Text,{as:"p",css:{color:"black",marginBottom:"0.5rem"},children:"• Platos: patatas, palomitas, boller\xeda/galletas y frutos secos."}),(0,s.tZ)(h.Text,{as:"p",css:{color:"black",marginBottom:"0.5rem"},children:"• A elegir o combinar: 4 Pizzas \xf3 4 roscas."}),(0,s.tZ)(h.Text,{as:"p",css:{color:"black",marginBottom:"1rem"},children:"• 5 Botellas de refresco."})]})]}),(0,s.BX)(h.Flex,{align:"start",className:"rx-Stack",direction:"row",gap:"3",children:[(0,s.tZ)(h.Box,{children:(0,s.tZ)("img",{css:{width:"280px",height:"auto"},src:"/pack_25_image.webp"})}),(0,s.BX)(h.Box,{css:{padding:"1rem",border:"2px solid #BE185D",borderRadius:"10px",marginBottom:"2rem",width:"100%"},children:[(0,s.tZ)(h.Heading,{css:{fontSize:"1.5rem",color:"#8B5CF6",marginBottom:"0.5rem"},children:"Pack para 25 Personas - 150€"}),(0,s.tZ)(h.Text,{as:"p",css:{color:"black",marginBottom:"0.5rem"},children:"• 50 Bocadillos \xf3 25 Sandwiches mixtos (o mitad y mitad)"}),(0,s.tZ)(h.Text,{as:"p",css:{color:"black",marginBottom:"0.5rem"},children:"• Platos: patatas, palomitas, boller\xeda/galletas y frutos secos"}),(0,s.tZ)(h.Text,{as:"p",css:{color:"black",marginBottom:"0.5rem"},children:"• A elegir o combinar: 4 Pizzas \xf3 4 roscas + 2 Tortillas de patatas"}),(0,s.tZ)(h.Text,{as:"p",css:{color:"black",marginBottom:"1rem"},children:"• 8 Botellas de refresco."})]})]}),(0,s.BX)(h.Flex,{align:"start",className:"rx-Stack",direction:"row",gap:"3",children:[(0,s.tZ)(h.Box,{children:(0,s.tZ)("img",{css:{width:"280px",height:"auto"},src:"/pack_30.jpeg"})}),(0,s.BX)(h.Box,{css:{padding:"1rem",border:"2px solid #BE185D",borderRadius:"10px",marginBottom:"2rem",width:"100%"},children:[(0,s.tZ)(h.Heading,{css:{fontSize:"1.5rem",color:"#8B5CF6",marginBottom:"0.5rem"},children:"Pack para 30 Personas - 180€"}),(0,s.tZ)(h.Text,{as:"p",css:{color:"black",marginBottom:"0.5rem"},children:"• 60 Bocadillos \xf3 30 Sandwiches mixtos (o mitad y mitad)"}),(0,s.tZ)(h.Text,{as:"p",css:{color:"black",marginBottom:"0.5rem"},children:"• Platos: patatas, palomitas, boller\xeda/galletas y frutos secos."}),(0,s.tZ)(h.Text,{as:"p",css:{color:"black",marginBottom:"0.5rem"},children:"• A elegir o combinar: 5 Pizzas \xf3 5 roscas + 2 Tortillas de patatas."}),(0,s.tZ)(h.Text,{as:"p",css:{color:"black",marginBottom:"1rem"},children:"• 10 Botellas de refresco."})]})]}),(0,s.BX)(h.Box,{css:{padding:"1rem",border:"2px solid #BE185D",borderRadius:"10px",color:"black",backgroundColor:"#e2d5f4 "},children:[(0,s.tZ)(h.Heading,{css:{fontSize:"2rem",color:"#BE185D",marginBottom:"1rem"},children:"Extras"}),(0,s.tZ)(h.Text,{as:"p",css:{marginBottom:"0.5rem"},children:"• Pizzas o roscas extras: 6€."}),(0,s.tZ)(h.Text,{as:"p",css:{color:"black",marginBottom:"0.5rem"},children:"• Botellas de refresco extras: 3,50€."}),(0,s.tZ)(h.Text,{as:"p",css:{color:"black",marginBottom:"0.5rem"},children:"• Botella de agua extra: 2,50€."}),(0,s.tZ)(h.Text,{as:"p",css:{color:"black",marginBottom:"0.5rem"},children:"• Bizcocho de cafeter\xeda (normal, de chocolate, con o sin cobertura) para 8 a 10 pax: 10€."}),(0,s.tZ)(h.Text,{as:"p",css:{marginBottom:"0.5rem"},children:"• Tarta de galletas de cafeter\xeda: 15€."}),(0,s.tZ)(h.Text,{as:"p",css:{color:"black",marginBottom:"0.5rem"},children:"• Tarta panader\xeda: 18€ el Kg."}),(0,s.tZ)(h.Text,{as:"p",css:{color:"black",marginBottom:"1rem"},children:"• Palmera de chocolate: 25€ (Con relleno Kinder: 28€)"})]})]}),(0,s.BX)(x(),{children:[(0,s.tZ)("title",{children:"MenaCumples | PacksInformation"}),(0,s.tZ)("meta",{content:"favicon.ico",property:"og:image"})]})]})}function k(){let[e,t]=(0,n.useContext)(i.EventLoopContext);return(0,s.tZ)(n.Fragment,{children:(0,c.isTrue)(t.length>0)?(0,s.tZ)(n.Fragment,{children:(0,s.tZ)(d.Z,{css:{color:"crimson",zIndex:9999,position:"fixed",bottom:"33px",right:"33px",animation:b+" 1s infinite"},size:32})}):(0,s.tZ)(n.Fragment,{})})}function _(){return(0,s.tZ)(Z,{})}},4511:function(e,t,r){"use strict";r.d(t,{SV:function(){return n}});var o=r(7294);let s=(0,o.createContext)(null),a={didCatch:!1,error:null};class n extends o.Component{constructor(e){super(e),this.resetErrorBoundary=this.resetErrorBoundary.bind(this),this.state=a}static getDerivedStateFromError(e){return{didCatch:!0,error:e}}resetErrorBoundary(){let{error:e}=this.state;if(null!==e){for(var t,r,o=arguments.length,s=Array(o),n=0;n<o;n++)s[n]=arguments[n];null===(t=(r=this.props).onReset)||void 0===t||t.call(r,{args:s,reason:"imperative-api"}),this.setState(a)}}componentDidCatch(e,t){var r,o;null===(r=(o=this.props).onError)||void 0===r||r.call(o,e,t)}componentDidUpdate(e,t){let{didCatch:r}=this.state,{resetKeys:o}=this.props;if(r&&null!==t.error&&function(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:[],t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:[];return e.length!==t.length||e.some((e,r)=>!Object.is(e,t[r]))}(e.resetKeys,o)){var s,n;null===(s=(n=this.props).onReset)||void 0===s||s.call(n,{next:o,prev:e.resetKeys,reason:"keys"}),this.setState(a)}}render(){let{children:e,fallbackRender:t,FallbackComponent:r,fallback:a}=this.props,{didCatch:n,error:i}=this.state,c=e;if(n){let e={error:i,resetErrorBoundary:this.resetErrorBoundary};if("function"==typeof t)c=t(e);else if(r)c=(0,o.createElement)(r,e);else if(void 0!==a)c=a;else throw i}return(0,o.createElement)(s.Provider,{value:{didCatch:n,error:i,resetErrorBoundary:this.resetErrorBoundary}},c)}}}},function(e){e.O(0,[49,888,774,179],function(){return e(e.s=762)}),_N_E=e.O()}]);