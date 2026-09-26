// api/video.js
export const config = {
  runtime: 'edge', // Use Edge runtime for efficient streaming
};

export default async function handler(request) {
  // 1. Get the token from Vercel's environment
  const token = process.env.GITHUB_ACCESS_TOKEN;
  if (!token) {
    return new Response('Server configuration error: missing token', { status: 500 });
  }

  // 2. Define the path to your video in the private repo
  const owner = '08Aristodemus24';
  const repo = 'project-alexander';
  const branch = 'master';
  const filePath = 'client-side/src/boards/compressed images/Skillsfinal.mp4';
  
  // 3. Construct the GitHub API URL
  // Using the 'contents' API allows us to fetch the raw file
  const githubApiUrl = `https://api.github.com/repos/${owner}/${repo}/contents/${encodeURIComponent(filePath)}?ref=${branch}`;

  // 4. Forward the browser's Range header to GitHub (crucial for video seeking)
  const rangeHeader = request.headers.get('range');

  try {
    const response = await fetch(githubApiUrl, {
      headers: {
        'Authorization': `Bearer ${token}`,
        'Accept': 'application/vnd.github.raw', // This tells GitHub to send the raw file
        ...(rangeHeader && { 'Range': rangeHeader }),
      },
    });

    if (!response.ok) {
      // If GitHub returns an error (e.g., 404), pass it through
      return new Response(`GitHub error: ${response.statusText}`, { status: response.status });
    }

    // 5. Stream the response back to the client
    // We forward the status (200 or 206 for partial content) and relevant headers
    const headers = new Headers(response.headers);
    // Ensure the browser knows it can seek
    headers.set('Accept-Ranges', 'bytes');
    // Prevent the browser from caching the raw token URL by mistake
    headers.set('Cache-Control', 'public, max-age=3600'); 

    return new Response(response.body, {
      status: response.status,
      headers: headers,
    });
  } catch (error) {
    console.error('Proxy error:', error);
    return new Response('Internal Server Error', { status: 500 });
  }
}