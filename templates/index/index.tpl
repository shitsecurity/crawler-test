% rebase('templates/core/index.tpl')
<h1>Index</h1>
<h2>Please view {{get_url('help')}} for help.</h2>
<p><a href="{{get_url('login_form')}}">Login</a></p>
<p><a href="{{get_url('login_form_csrf')}}">Login CSRF</a></p>
<p><a href="{{get_url('profile')}}">Profile</a></p>
<p><a href="{{get_url('depth')}}">Depth</a></p>
<p><a href="{{get_url('width')}}">Width</a></p>
<p><a href="{{get_url('cycle')}}">Cycle</a></p>
<p><a href="{{get_url('mixed')}}">Mixed</a></p>
<p><a href="{{get_url('submit_form')}}">Submit</a></p>
<p><a href="{{get_url('get')}}?p1=index&p2=1">GET</a></p>
<p>Secret: {{get_url('secret')}}</p>
<p>Robots: {{get_url('robots')}}</p>
<p>Sitemap: {{get_url('sitemap')}}</p>
