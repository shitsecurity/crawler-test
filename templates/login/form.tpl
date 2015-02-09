% rebase('templates/core/index.tpl')
<form method="POST" action="{{get_url('login')}}">
	<input type="text" name="login">
	<input type="password" name="password">
	<input type="submit" value="Go">
</form>
