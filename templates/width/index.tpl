% rebase('templates/core/index.tpl')
<h1>Width</h1>
% for ii in xrange(get('amount',0)):
<p><a href="{{get_url('width')}}{{ii}}">Link {{ii}}</a></p>
% end
