/* Taelgar qualitative weather-pattern atlas, 2026-09-26.
 * Build: node build.cjs [basemap.jpg] [output-directory]
 * Requires sharp. All overlays use the existing 1907 x 1280 map reference frame.
 * Geometry is schematic: it does not assign pressure contours, rain boundaries,
 * snowlines, storm frequency, exact passes, or a synchronized continental cycle.
 */
const fs = require('fs');
const path = require('path');
let sharp;
try { sharp = require('sharp'); } catch {
  sharp = require('/Users/tim/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
}
const base = process.argv[2] || '/Users/tim/Library/CloudStorage/Dropbox/TaeglarMaps/WorldMap/taelgar-basemap.jpg';
const out = process.argv[3] || '/tmp/taelgar-connected-weather/rendered';
fs.mkdirSync(out, {recursive:true});
const C = {paper:'#faf9f4', ink:'#243b43', muted:'#63777d', rule:'#c3cecd', wind:'#703e91', track:'#293a48', high:'#bb5a2f', low:'#467bb2', wet:'#21806b', snow:'#238bac', magic:'#976689'};
const esc = s => String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');
function text(x,y,s,size=14,color=C.ink,weight=600,anchor='start',halo=3) {
  return `<text x="${x}" y="${y}" font-size="${size}" fill="${color}" font-weight="${weight}" text-anchor="${anchor}" paint-order="stroke" stroke="${C.paper}" stroke-width="${halo}" stroke-linejoin="round">${String(s).split('\n').map((l,i)=>`<tspan x="${x}" dy="${i ? size*1.26 : 0}">${esc(l)}</tspan>`).join('')}</text>`;
}
const defs = `<defs>
  <marker id="wind-arrow" markerWidth="13" markerHeight="12" refX="11" refY="6" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0 L13 6 L0 12 Z" fill="${C.wind}"/></marker>
  <marker id="track-arrow" markerWidth="15" markerHeight="14" refX="12" refY="7" orient="auto" markerUnits="userSpaceOnUse"><path d="M1 1 L8 7 L1 13 M7 1 L14 7 L7 13" fill="none" stroke="${C.track}" stroke-width="2.2"/></marker>
  <pattern id="snow-hatch" width="9" height="9" patternUnits="userSpaceOnUse"><path d="M-2 2 L2 -2 M0 9 L9 0 M7 11 L11 7" stroke="${C.snow}" stroke-width="1.2" stroke-opacity=".5"/></pattern>
  <pattern id="magic-hatch" width="12" height="12" patternUnits="userSpaceOnUse"><path d="M0 0 L12 12 M0 12 L12 0" stroke="${C.magic}" stroke-width=".7" stroke-opacity=".32"/></pattern>
  <pattern id="rain-dots" width="12" height="12" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r="1.1" fill="${C.wet}" fill-opacity=".4"/></pattern>
  </defs>`;
function arrow(d,kind='wind',w=3.3) {
  return `<path d="${d}" fill="none" stroke="${C.paper}" stroke-width="${w+3}" stroke-linecap="round"/><path d="${d}" fill="none" stroke="${C[kind]}" stroke-width="${w}" stroke-linecap="round" ${kind==='track'?'stroke-dasharray="9 6"':''} marker-end="url(#${kind}-arrow)"/>`;
}
function area(d,kind,opacity=.13,pattern) {
  return `<path d="${d}" fill="${C[kind]}" fill-opacity="${opacity}" stroke="${C[kind]}" stroke-opacity=".7" stroke-width="1.3" stroke-dasharray="5 4"/>${pattern?`<path d="${d}" fill="url(#${pattern})"/>`:''}`;
}
function badge(x,y,n) {
  return `<circle cx="${x}" cy="${y}" r="14" fill="${C.ink}" stroke="${C.paper}" stroke-width="2"/>${text(x,y+5,n,14,C.paper,700,'middle',0)}`;
}
function note(x,y,s,color=C.muted,size=13) {return text(x,y,s,size,color,550,'middle');}
function geo(summer=false) {
  let s='';
  const names=[
    [156,293,'Mawakel',13],[335,282,'Slate Sea',11],
    [384,335,'Fiatara',12],[443,385,'Voltara',12],[473,300,'Erbalta',12],
    [296,399,'Tawir',11],[346,492,'Lake\nValandros',12],
    [474,546,'Ainumarya',12],[461,625,'Elderwood',11],
    [238,551,'Coastlands',12],[310,653,'Chardon',14],
    [100,857,'Apporia',13],[281,790,'Emerald Bay',11],
    [645,638,'Aurbez',12],[738,606,'Maseau',11],[813,572,'Tyrwingha',11],
    [736,491,'SEMBARA',17],[870,317,'Vostok',14],[1285,337,'URSK',18],
    [885,524,'Western\nGulf',11],[973,560,'Cymea',15],
    [1335,565,'IRRLA',17],[1594,833,'Medju',12],
    [495,851,'Darba',12],[650,859,'Hara Basin',13],
    [662,925,'Yuvanti',12],[752,960,'Garamjala',12]
  ];
  for (const a of names) s+=text(...a,C.muted,600,'middle',3.4);
  s+=text(695,362,'SENTINELS',14,C.muted,700,'middle')+text(676,757,'DUNMAR',17,C.muted,700,'middle');
  s+=note(1360,1030,'REGIONAL PATTERNS UNASSIGNED',C.muted,16)+note(1360,1057,'Unshaded country is not necessarily dry.',C.muted,13);
  s+=text(70,1075,'NEVOS SEA',16,C.muted,650)+text(1430,665,'GREEN SEA',17,C.muted,650);
  s+=text(47,470,'ENDLESS',13,C.muted,550)+text(47,489,'OCEAN',13,C.muted,550);
  s+=text(1845,1134,'N',16,C.ink,700,'middle')+`<path d="M1845 1177 V1146 M1839 1155 L1845 1145 L1851 1155" fill="none" stroke="${C.ink}" stroke-width="2"/>`;
  return s;
}
const D={
  westWinter:'M10 920 C15 850 110 802 225 807 C342 800 412 861 398 940 C377 1004 262 1029 135 1000 C53 983 15 958 10 920 Z',
  westStrong:'M100 412 C148 384 197 403 235 455 C270 483 363 475 443 532 C479 579 439 656 355 701 C273 748 135 764 59 708 C12 669 21 597 67 550 C96 511 69 450 100 412 Z',
  westWeak:'M69 605 C121 552 195 553 256 585 C325 600 387 620 405 656 C398 707 331 745 232 752 C128 760 47 718 46 672 C44 645 53 625 69 605 Z',
  eastWinter:'M1070 820 C1086 758 1230 739 1400 750 C1587 744 1688 767 1705 820 C1724 886 1590 932 1430 933 C1249 942 1100 897 1070 820 Z',
  eastSummer:'M1128 591 C1176 532 1254 512 1380 515 C1520 510 1613 532 1657 575 C1696 624 1647 680 1550 704 C1431 730 1276 699 1184 661 C1135 640 1116 617 1128 591 Z',
  northStrong:'M688 283 C737 223 920 199 1108 218 C1280 216 1435 224 1480 275 C1492 323 1392 359 1260 364 C1077 365 878 331 736 335 C712 324 695 306 688 283 Z',
  northInterrupted:'M850 269 C914 213 1050 212 1160 222 C1309 223 1439 237 1475 280 C1486 321 1397 354 1260 360 C1117 362 975 329 891 321 C861 309 846 290 850 269 Z',
  cymea:'M889 484 C846 504 834 567 848 630 C859 693 898 759 954 785 C1007 799 1046 760 1062 704 C1078 649 1051 593 1035 550 C1024 517 1030 505 1077 498 C1230 489 1430 508 1653 489 L1657 455 C1420 443 1222 443 1090 450 C1002 455 938 462 889 484 Z',
  magic:'M1806 241 C1770 340 1800 384 1780 459 C1753 542 1788 603 1766 680 C1745 747 1762 828 1758 916 L1895 916 L1895 241 Z',
  westRain:'M123 285 C190 248 252 323 268 359 C313 322 346 282 381 282 L411 363 C415 411 478 419 509 468 C537 522 503 590 486 666 C418 711 343 726 266 708 C212 676 232 603 211 548 C180 471 234 434 196 387 C145 365 111 330 123 285 Z',
  forestRain:'M161 395 C211 364 257 381 303 400 C364 408 433 423 481 461 C530 501 507 551 485 594 C465 626 464 659 428 676 C386 681 369 645 350 608 C332 561 305 526 258 501 C192 464 147 437 161 395 Z',
  sembaraRain:'M805 427 C858 413 915 427 937 467 C892 486 856 512 821 538 C785 582 730 589 686 566 C650 544 638 503 661 467 C701 437 751 447 805 427 Z',
  sembaraWinterRain:'M786 422 C852 411 913 431 939 466 C907 491 896 539 861 562 C811 605 769 620 720 596 C684 580 643 531 650 487 C673 447 735 444 786 422 Z',
  westSnow:'M540 266 C584 263 609 288 628 324 C601 343 596 377 597 412 C620 445 630 475 602 502 C578 523 587 563 611 601 C605 636 635 672 655 712 L644 744 C599 720 579 682 561 644 C531 612 541 568 541 535 C525 510 507 474 527 439 C550 404 535 359 546 323 C518 302 519 282 540 266 Z',
  fiataraSnow:'M365 277 C395 272 418 300 411 327 C407 345 393 361 383 364 L364 345 C375 324 352 301 365 277 Z',
  eastSnow:'M636 377 C662 393 650 427 663 455 C686 480 675 524 661 552 C657 581 688 608 708 631 L695 654 C661 632 636 603 628 575 C630 551 609 530 623 501 C639 476 618 443 623 419 Z',
  summerUplift:'M621 403 C653 411 651 439 661 462 C687 493 672 531 654 552 C628 566 612 548 617 525 C640 500 610 477 617 449 C614 428 606 419 621 403 Z',
  dunmarRain:'M324 787 C363 753 429 781 475 789 C529 788 585 777 627 793 C666 805 693 830 719 860 L698 904 C659 930 619 948 577 965 C535 987 468 1032 429 1020 C407 1000 427 964 441 930 C442 889 421 852 399 825 C365 822 337 813 324 787 Z',
  southernFringe:'M499 768 C535 737 579 718 626 734 L671 764 L640 793 C599 781 559 786 520 798 Z'
};
function magicalContext() {
  return area(D.magic,'magic',.045,'magic-hatch')+text(1837,535,'MAGICAL',12,C.magic,650,'middle')+text(1837,553,'STORM ZONE',12,C.magic,650,'middle')+note(1837,580,'Eastern Isles',C.magic,11);
}
function winterContext() {
  return area(D.westWinter,'high',.11)+text(200,910,'H',31,C.high,600,'middle')+note(201,941,'Western ridge',C.high,13)+note(201,960,'winter position',C.high,11)+
    area(D.eastWinter,'high',.10)+text(1410,841,'H',31,C.high,600,'middle')+note(1388,878,'Green Sea winter ridge',C.high,14)+
    magicalContext()+arrow('M1060 420 C1228 428 1454 421 1635 405','wind',2.5)+note(1350,395,'Northern winter westerlies',C.wind,13);
}
function summerContext(weak=false) {
  let s=area(weak?D.westWeak:D.westStrong,'high',.12)+text(211,659,'H',31,C.high,600,'middle')+note(200,700,'Chardon ridge',C.high,14);
  s+=area(weak?D.northInterrupted:D.northStrong,'high',.09)+text(1100,275,'H',31,C.high,600,'middle')+note(1100,305,'Recurring Urskan ridge',C.high,14);
  s+=area(D.eastSummer,'high',.11)+text(1420,572,'H',31,C.high,600,'middle')+note(1445,606,'Green Sea summer ridge',C.high,14);
  s+=area(D.cymea,'low',.075)+text(952,639,'L',30,C.low,600,'middle')+note(966,676,'Cymean low',C.low,14)+note(1390,481,'Lower-pressure corridor',C.low,12);
  s+=magicalContext()+arrow('M1595 415 C1430 416 1235 424 1057 424','wind',2.5)+note(1357,401,'Northern E–NE winds',C.wind,13);
  s+=arrow('M1112 735 C1101 662 1097 603 1117 546','wind',2.5)+arrow('M1665 547 C1713 591 1716 658 1670 717','wind',2.5)+arrow('M1572 741 C1454 768 1325 749 1236 720','wind',2.5);
  s+=note(1180,696,'Northward\noffshore air',C.wind,11);
  return s;
}
function greenSeaInflow() {return arrow('M943 444 C875 454 813 499 763 549')+arrow('M795 464 Q725 468 650 512', 'wind',2.5);}
function winterWest(){return {
  number:'01', slug:'winter-western-approach', title:'Winter · the western approach',
  sub:'Ocean disturbances wet the western slopes; much of the moisture falls before crossing the Sentinels.',
  draw:()=>winterContext()+area(D.westRain,'wet',.16,'rain-dots')+area(D.westSnow,'snow',.10,'snow-hatch')+area(D.fiataraSnow,'snow',.12,'snow-hatch')+
    arrow('M24 326 C113 332 194 351 263 387')+arrow('M91 537 C213 504 372 523 518 500')+arrow('M116 628 Q229 600 352 617')+
    arrow('M34 548 C243 538 414 589 559 605','track',3.2)+
    note(491,196,'Northern maritime storms also\nbring Fiatara mountain snow.',C.snow,13)+
    note(761,717,'Sheltered interior:\nless western moisture',C.muted,13)+
    badge(129,354,1)+badge(448,475,2)+badge(627,584,3),
  cards:[['1 · Western ocean supply','Mawakel has milder rain-and-thaw intervals.','Cold outbreaks between storms can bring coastal snow.'],['2 · Exposed mountains','Rain increases over western forests and slopes.','Snow accumulates in sufficiently cold high country.'],['3 · The range separates the flows','The western side loses much of the incoming moisture.','An upper-air disturbance can still continue east.']],
  caveat:'A representative winter approach, not a requirement that one storm wet the whole western coast at once.'
};}
function winterEast(){return {
  number:'02', slug:'winter-eastern-redevelopment',title:'Winter · redevelopment east of the mountains',
  sub:'The disturbance continues east; a reorganizing low draws a fresh moisture supply inland from the Green Sea.',
  draw:()=>winterContext()+area(D.sembaraWinterRain,'wet',.17,'rain-dots')+area(D.eastSnow,'snow',.10,'snow-hatch')+
    `<ellipse cx="835" cy="621" rx="56" ry="37" fill="${C.low}" fill-opacity=".10" stroke="${C.low}" stroke-width="1.6" stroke-dasharray="5 4"/>`+
    text(835,627,'L',29,C.low,650,'middle')+
    arrow('M467 572 C548 557 598 584 641 613','track',2.8)+arrow('M661 622 C740 647 835 636 959 584 S1109 528 1205 460','track',3.2)+
    arrow('M951 456 C875 459 804 478 721 523')+arrow('M912 519 Q824 516 679 563','wind',2.8)+
    note(420,512,'Western rain eases',C.muted,14)+
    note(732,682,'Candidate low corridor',C.low,13)+note(771,703,'Maseau–Mostreve → Tyrwingha / Cymea',C.low,11)+
    note(1110,588,'Some lows strengthen\nfarther offshore.',C.low,13)+
    note(845,1060,'Cold or drier air follows as the low departs;\nclearing does not mean a warm winter.',C.muted,13)+
    badge(598,603,1)+badge(765,459,2)+badge(1005,599,3),
  cards:[['1 · A moving weather system','Dashed arrows trace the eastward disturbance / low.','They do not show the local wind direction.'],['2 · An eastern moisture source','Air north of the low moves westward into Sembara.','Rain or snow depends on the cold air already present.'],['3 · Sheltered Gulf, open-sea growth','Ordinary Gulf rainmakers can be comparatively weak.','Not every western storm develops into this sequence.']],
  caveat:'Second stage of a possible winter sequence. Hatching highlights mountain snow potential, not the full extent of lowland snowfall.'
};}
function summerRidge(){return {
  number:'03',slug:'summer-ridge-and-eastern-inflow',title:'Summer · western ridge, eastern maritime inflow',
  sub:'A settled western interval can coexist with Green Sea moisture reaching Sembara and the eastern Sentinel slopes.',
  draw:()=>summerContext(false)+area(D.sembaraRain,'wet',.16,'rain-dots')+area(D.summerUplift,'wet',.19,'rain-dots')+greenSeaInflow()+
    arrow('M29 311 Q87 311 139 321')+arrow('M178 447 Q212 504 211 576')+
    note(291,221,'Mawakel stays beyond\nthe seasonal ridge.',C.wind,13)+
    note(403,444,'Drying reaches inland',C.high,12)+
    note(565,875,'Aurbez / Maseau keep their dry summer tendency;\neastern moisture does not wet every valley equally.',C.muted,13)+
    badge(303,571,1)+badge(690,516,2)+badge(1157,236,3),
  cards:[['1 · One western ridge','The Chardon ridge extends north, ending south of Mawakel.','Its variable inland reach can dry Valandros and the forests.'],['2 · Moisture from the other side','NE–SW maritime air reaches Sembara and exposed slopes.','The Sentinels limit how much reaches the western side.'],['3 · Recurring summer pressure','The northern ridge supports Green Sea E–NE winds.','Breaks and disturbances remain part of the season.']],
  caveat:'A settled western episode, not a rain-free summer. Rain shading marks favored precipitation areas, not continuous rain.'
};}
function summerWest(){return {
  number:'04',slug:'summer-western-wet-spell',title:'Summer · a western wet spell',
  sub:'The northern ridge influence retreats, allowing ocean moisture through the Coastlands to Valandros and the forests.',
  draw:()=>summerContext(true)+area(D.forestRain,'wet',.18,'rain-dots')+
    area('M128 284 C164 263 223 302 261 341 L249 394 C204 385 178 368 146 347 Z','wet',.14,'rain-dots')+
    area('M385 352 C414 342 449 356 473 382 L459 414 C426 419 399 405 385 382 Z','wet',.09,'rain-dots')+
    area(D.sembaraRain,'wet',.09,'rain-dots')+greenSeaInflow()+
    arrow('M31 335 Q121 345 200 365')+arrow('M110 534 C204 505 323 465 478 454')+
    arrow('M279 425 Q352 411 427 376','wind',2.8)+
    arrow('M52 407 C210 389 380 403 541 435','track',3.2)+arrow('M557 437 Q643 427 745 462','track',2.3)+
    note(197,237,'Unsettled weather\nreturns to Mawakel.',C.wind,13)+
    note(693,718,'Some disturbances cross and help trigger eastern rain;\nothers weaken or remain west of the range.',C.muted,13)+
    badge(308,460,1)+badge(466,586,2)+badge(359,648,3),
  cards:[['1 · The upwind corridor also changes','Wet weather crosses the northern Coastlands.','Occasional SW access also brings rain toward Voltara.'],['2 · Repeated forest moisture','Valandros and Ainumarya receive recurring wet spells.','Rain increases on exposed rising ground.'],['3 · Chardon can remain dry','The southern ridge persists as its northern reach retreats.','Eastern rain need not alternate in lockstep with western rain.']],
  caveat:'A wet interruption within summer. The western reach of the northern ridge is interrupted here; regional ridges later rebuild.'
};}
function monsoon(){return {
  number:'05',slug:'active-dunmari-monsoon',title:'Summer · an active Dunmari monsoon spell',
  sub:'Nevos moisture reaches Dunmar and some southern Sentinel approaches, with strong terrain control farther inland.',
  draw:()=>summerContext(false)+area(D.dunmarRain,'wet',.19,'rain-dots')+area(D.southernFringe,'wet',.085,'rain-dots')+
    area(D.sembaraRain,'wet',.09,'rain-dots')+greenSeaInflow()+
    `<path d="M264 775 C357 737 481 743 589 774" fill="none" stroke="${C.low}" stroke-width="2" stroke-dasharray="4 5"/>`+
    note(300,735,'Nevos monsoon trough',C.low,12)+
    arrow('M255 901 Q351 883 460 835')+arrow('M285 984 Q361 960 437 922')+
    arrow('M337 849 Q390 827 440 799','wind',3.1)+arrow('M491 813 Q537 782 591 760','wind',2.6)+
    note(767,829,'Less reliable rain\nfarther inland',C.wet,12)+
    note(440,1090,'W–SW air from the Nevos',C.wind,14)+
    note(1090,949,'The two monsoons have different moisture sources.\nNo continuous Nevos-to-Sembara trough is assigned.',C.muted,14)+
    badge(391,901,1)+badge(576,757,2)+badge(662,680,3),
  cards:[['1 · Active western / southwestern inflow','Nevos air supplies Dunmar; Emerald Bay is a shifting fringe.','Mountains and distance reduce rain toward the interior.'],['2 · Southern mountain margins','Cloud and rain sometimes reach exposed foothills and valleys.','The shaded fringe does not define a pass or a fixed boundary.'],['3 · The dry interior is retained','Aurbez and the high interior do not acquire a full wet summer.','Southern high-country snow remains mainly a winter supply.']],
  caveat:'An active spell, not an onset calendar. The separate Green Sea summer circulation is shown for geographical context.'
};}
const specs=[winterWest(),winterEast(),summerRidge(),summerWest(),monsoon()];
function legend() {
  let s=arrow('M54 161 H113')+text(132,170,'Air movement',24,C.wind,550);
  s+=arrow('M415 161 H485','track')+text(503,170,'Moving disturbance / low',24,C.track,550);
  s+=`<rect x="1013" y="147" width="39" height="24" rx="4" fill="${C.high}" fill-opacity=".16" stroke="${C.high}"/>`+text(1070,170,'H  Ridge',24,C.high,550);
  s+=`<rect x="1335" y="147" width="39" height="24" rx="4" fill="${C.low}" fill-opacity=".15" stroke="${C.low}"/>`+text(1392,170,'L  Low / trough',24,C.low,550);
  s+=`<rect x="1773" y="146" width="39" height="25" fill="${C.wet}" fill-opacity=".22"/>`+text(1830,170,'Favored rain / snow',24,C.wet,550);
  s+=`<rect x="2290" y="146" width="39" height="25" fill="url(#snow-hatch)" stroke="${C.snow}"/>`+text(2347,170,'Mountain snow',24,C.snow,550);
  return s;
}
async function main(){
  const raw=await sharp(base).resize(3300,2215,{fit:'fill'}).jpeg({quality:88}).toBuffer();
  const image=`<image x="0" y="0" width="1907" height="1280" href="data:image/jpeg;base64,${raw.toString('base64')}"/><rect width="1907" height="1280" fill="${C.paper}" opacity=".48"/>`;
  const manifest={title:'Taelgar connected weather patterns',date:'2026-09-26',source:'Background/Taelgar Climatic Model.md and the accompanying Sentinel integration discussion',basemap:path.basename(base),frame:[1907,1280],status:'Qualitative review diagrams. Sentinel integration is proposed development; areas and arrows are schematic.',maps:[]};
  for(const v of specs){
    let s=`<svg xmlns="http://www.w3.org/2000/svg" width="3200" height="2590" viewBox="0 0 3200 2590"><title>${esc(v.title)}</title><desc>${esc(v.sub+' '+v.caveat+' Full original basemap extent; north up. Purple arrows show air movement. Dark dashed double-headed-chevron arrows show system movement. Colors describe illustrative conditions and pressure influence, not measured values. Unshaded areas have no condition assigned on this plate. The Eastern Isles storm zone is magical. Ocean currents are not shown.')}</desc>${defs}<rect width="3200" height="2590" fill="${C.paper}"/><g font-family="Arial, Helvetica, sans-serif">`;
    s+=text(54,49,'TAELGAR  /  CONNECTED WEATHER PATTERNS',23,C.muted,600)+text(3146,50,v.number+' / 05',23,C.muted,600,'end');
    s+=text(54,100,v.title,39,C.ink,650)+text(54,132,v.sub,23,C.muted,400)+legend();
    s+=`<svg x="54" y="204" width="3092" height="2075.42" viewBox="0 0 1907 1280">${image}${v.draw()}${geo(v.number>='03')}</svg><rect x="54" y="204" width="3092" height="2075.42" fill="none" stroke="${C.rule}" stroke-width="1.5"/>`;
    for(let i=0;i<3;i++){
      const x=54+i*1046;
      s+=text(x,2331,v.cards[i][0],25,C.ink,650)+text(x,2367,v.cards[i][1],22,C.muted,400)+text(x,2397,v.cards[i][2],22,C.muted,400);
    }
    s+=`<path d="M54 2430 H3146" stroke="${C.rule}"/>`+text(54,2466,v.caveat,22,C.ink,500);
    s+=text(54,2506,'SCHEMATIC REVIEW MAPS · Pressure influence, rain areas and tracks have no fixed boundaries or assigned strength.',21,C.muted,400);
    s+=text(54,2542,'The five plates are examples, not a synchronized seasonal sequence. Unmodeled regions remain visible.',21,C.muted,400)+text(3146,2542,'NORTH UP · FULL BASEMAP EXTENT',20,C.muted,500,'end');
    s+='</g></svg>';
    const stem='taelgar-'+v.slug+'-v1';
    fs.writeFileSync(path.join(out,stem+'.svg'),s);
    await sharp(Buffer.from(s)).png().toFile(path.join(out,stem+'.png'));
    await sharp(Buffer.from(s)).resize(1700).png().toFile('/tmp/taelgar-connected-weather/'+v.number+'-preview.png');
    manifest.maps.push({number:v.number,title:v.title,stem,interpretation:v.sub,notes:v.cards,caveat:v.caveat});
    console.log(stem);
  }
  fs.writeFileSync(path.join(out,'manifest.json'),JSON.stringify(manifest,null,2)+'\n');
  const tiles=[];
  for(let i=0;i<5;i++)tiles.push({input:await sharp(path.join(out,manifest.maps[i].stem+'.png')).resize(1160).png().toBuffer(),left:40+(i%3)*1200,top:160+Math.floor(i/3)*1030});
  const cover=`<svg width="1160" height="939"><rect width="1160" height="939" fill="${C.paper}"/><g font-family="Arial, Helvetica, sans-serif">${text(50,90,'READING THE SET',35,C.ink,650)}${text(50,160,'01 → 02',32,C.low,650)}${text(50,206,'Two stages of a possible winter storm.',27,C.muted,400)}${text(50,302,'03 ↔ 04',32,C.high,650)}${text(50,348,'Contrasting western summer episodes.',27,C.muted,400)}${text(50,444,'05',32,C.wet,650)}${text(50,490,'An active Dunmari monsoon spell.',27,C.muted,400)}${text(50,604,'Same geography and extent on every plate.',28,C.ink,550)}${text(50,658,'Arrows separate winds from system movement.',25,C.muted,400)}${text(50,700,'Shading is illustrative, not a rainfall total.',25,C.muted,400)}${text(50,742,'Unshaded areas are not necessarily dry.',25,C.muted,400)}${text(50,838,'Open the individual maps to read local details.',25,C.muted,400)}</g></svg>`;
  tiles.push({input:Buffer.from(cover),left:2440,top:1190});
  const head=`<svg width="3640" height="120"><g font-family="Arial,Helvetica,sans-serif">${text(40,55,'TAELGAR · HOW THE REGIONAL WEATHER SYSTEMS CONNECT',38,C.ink,650)}${text(40,101,'Five qualitative maps over the unchanged continental basemap · September 2026',25,C.muted,400)}</g></svg>`;
  tiles.push({input:Buffer.from(head),left:0,top:0});
  await sharp({create:{width:3640,height:2210,channels:3,background:C.paper}}).composite(tiles).png().toFile(path.join(out,'taelgar-connected-weather-overview-v1.png'));
}
main().catch(e=>{console.error(e);process.exitCode=1;});
