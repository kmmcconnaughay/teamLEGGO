_satellite.pushAsyncScript(function(event, target, $variables){
  if (_satellite.getVar('over13') && !_satellite.getVar('decibleLoaded')) {
// <![CDATA[
	(function(d,e,c,i,b,el,it) {
		d._da_=d._da_||[];_da_.oldErr=d.onerror;_da_.err=[];
		d.onerror=function(){_da_.err.push(arguments);_da_.oldErr&&_da_.oldErr.apply(d,Array.prototype.slice.call(arguments));};
		d.DecibelInsight=b;d[b]=d[b]||function(){(d[b].q=d[b].q||[]).push(arguments);};
		el=e.createElement(c),it=e.getElementsByTagName(c)[0];el.async=1;el.src=i;el.id="decibelInsight";it.parentNode.insertBefore(el,it);
	})(window,document,'script','https://shop.lego.com/static/javascript/vendor/di.min.js','decibelInsight');
// ]]>
  _satellite.setVar('decibleLoaded', true);
}
else {
  _satellite.setVar('decibleLoaded', false);
}

});
