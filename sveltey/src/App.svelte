<!-- App.svelte -->
<script>
  import demise from './pages/demise.svelte';
  import pvp from './pages/pvp.svelte';
  import '@fontsource/bad-script';
  import { Router, Link, Route } from 'svelte-routing';
  export let url = '';
</script>

<Router {url}>
  {#if url === undefined}
    <p>Error: URL is undefined</p>
  {/if}
  <nav>
    <Link to="/">Demise</Link>
    <Link to="/pvp">PvP</Link>
  </nav>
  <Route path="/" component={demise} />
  <Route path="/pvp" component={pvp} />
</Router>



<style>
  :global(h1, body, textarea, input) {
    font-family: "bad script";
  }

  nav {
    color: white;
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-bottom: 1rem;
  }

  nav :global(a) {
    color: white;
    text-decoration: none;
  }

  nav :global(a:hover) {
    text-decoration: underline;
  }

  nav :global(.active) {
    font-weight: bold;
  }
</style>