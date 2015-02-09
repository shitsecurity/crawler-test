% rebase('templates/core/index.tpl')
<form method="POST" action="{{get_url('login_csrf')}}">
	<input type="text" name="login">
	<input type="password" name="password">
	<input type="submit" value="Go">
	<input type="hidden" name="token" value="{{token}}">
</form>
