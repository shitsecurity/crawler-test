% rebase('templates/core/index.tpl')
<h1>Depth</h1>
% for link in links:
	<p><a href={{link}}>{{link}}</a></p>
% end
