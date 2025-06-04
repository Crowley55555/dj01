"""
Views for the AI Blog application.

Contains view functions for rendering data and test pages.
"""
from django.shortcuts import render


def data_page(request):
    """
    Renders the data page with AI-related content about data science.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse with rendered data.html template
    """
    context = {
        'title': 'Data Science in AI',
        'articles': [
            {
                'title': 'The Future of Big Data in AI',
                'summary': 'How massive datasets are shaping the next generation of AI models.',
                'author': 'Dr. Data'
            },
            {
                'title': 'Data Labeling Techniques',
                'summary': 'Comparative analysis of manual vs automated data labeling approaches.',
                'author': 'Label Master'
            },
            {
                'title': 'Data Privacy in ML',
                'summary': 'Ensuring privacy while training models on sensitive data.',
                'author': 'Privacy Guardian'
            }
        ],
        'trends': [
            'Synthetic data generation',
            'Federated learning',
            'Data-centric AI'
        ]
    }
    return render(request, 'ai_blog/data.html', context)


def test_page(request):
    """
    Renders the test page with AI testing and evaluation content.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse with rendered test.html template
    """
    context = {
        'title': 'AI Testing Methodologies',
        'articles': [
            {
                'title': 'Benchmarking AI Models',
                'summary': 'Comprehensive guide to evaluating model performance across different metrics.',
                'author': 'Benchmark Pro'
            },
            {
                'title': 'Adversarial Testing',
                'summary': 'How to test your models against adversarial attacks and edge cases.',
                'author': 'Security Expert'
            },
            {
                'title': 'A/B Testing for AI Products',
                'summary': 'Practical approaches to A/B testing for AI-powered features.',
                'author': 'Product Scientist'
            }
        ],
        'methodologies': [
            'Unit testing for ML',
            'Integration testing',
            'Performance benchmarking',
            'Bias and fairness evaluation'
        ]
    }
    return render(request, 'ai_blog/test.html', context)

def home_page(request):
    """
    Renders the home page of the AI blog.
    """
    context = {
        'title': 'CyberBlog AI - Home',
        'featured_articles': [
            {
                'title': 'Introduction to Artificial Intelligence',
                'summary': 'Learn the basics of AI and its applications in modern technology.',
                'url': 'data'
            },
            {
                'title': 'Testing AI Systems',
                'summary': 'Discover best practices for testing and validating AI models.',
                'url': 'test'
            }
        ]
    }
    return render(request, 'ai_blog/home.html', context)
