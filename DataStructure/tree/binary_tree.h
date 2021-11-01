/* Binary Tree header file
 * This header file is for each binary tree structure and operations.
 */

typedef int BData; // data type for item //
#define max(a,b)  (((a) > (b)) ? (a) : (b))  // get max of two numbers //

typedef struct _bTreeNode
{	// C style binary tree struct //
	BData item;
	struct _bTreeNode *left_child;
	struct _bTreeNode *right_child;
} BTreeNode;

// Operations //
BTreeNode *createNode(BData item)
{	// Create a new node //
	BTreeNode *node = (BTreeNode *)malloc(sizeof(BTreeNode));
	node->item = item;
	node->left_child = NULL;
	node->right_child = NULL;

	return node;
}
void destroyNode(BTreeNode *node)
{	// Destroy a node //
	free(node);
}

// Connect the root to a child node //
void createLeftSubtree(BTreeNode* root, BTreeNode *left)
{	// Connect the root to a left-side node //
	if(root->left_child != NULL)
		exit(1);
	
	root->left_child = left;
}
void createRightSubtree(BTreeNode* root, BTreeNode *right)
{	// Connect the root to a right-side node //
	if(root->right_child != NULL)
		exit(1);
	
	root->right_child = right;
}

// Trevers a tree //
void travel_inorder(BTreeNode *root)
{	// Travel the binary tree inorder(LCR) //
	if(root != NULL)
	{
		travel_inorder(root->left_child);
		printf("%d ", root->item);
		travel_inorder(root->right_child);
	}
}
void travel_preorder(BTreeNode *root)
{	// Travel the binary tree preorder(CLR) //
	if(root != NULL)
	{
		printf("%d ", root->item);
		travel_inorder(root->left_child);
		travel_inorder(root->right_child);
	}
}
void travel_postorder(BTreeNode *root)
{	// Travel the binary tree postorder(LRC) //
	if(root != NULL)
	{		
		travel_inorder(root->left_child);
		travel_inorder(root->right_child);
		printf("%d ", root->item);
	}
}
/* levelorder needs queue headerfile
void travel_levelorder(BTreeNode *root)
{	// Travel the binary tree levelorder //
	Queue queue;
	if(root == NULL) return ;

	initQueue(&quque);
	enqueue(&queue, root);
	while(isQueueEmpty(&queue))
	{
		root = peekQueue(*queue);
		dequeue(&queue);

		printf("%d ", root->item);
		if(root->left_child != NULL)
			enqueue(&queue, root->left_child);
		if(root->right_child != NULL)
			enqueue(&queue, root->right_child);
	}
}
*/

// Extra operatoins //
int getNodeNum(BTreeNode *node)
{	// Get number of nodes //
	int l = 0, r = 0;
	if(node->left_child != NULL)
		l = getNodeNum(node->left_child);
	if(node->right_child != NULL)
		r = getNodeNum(node->right_child);
	
	return 1 + l + r;
}
int getHeight(BTreeNode *node)
{
	int l = 0, r = 0;
	if(node->left_child != NULL)
		l = getHeight(node->left_child);
	if(node->right_child != NULL)
		r = getHeight(node->right_child);

	return 1 + max(l, r);
}